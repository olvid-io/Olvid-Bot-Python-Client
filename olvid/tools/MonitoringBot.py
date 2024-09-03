import asyncio
import os
import json
from asyncio import iscoroutine

from typing import Callable, Optional, Coroutine, Union, Any

# for compatibility with python 3.10
from typing import TypeVar
# noinspection PyTypeHints
Self = TypeVar("MonitoringBot")

from .logger import tools_logger

# if aiohttp is not installed we use urllib run in executor to avoid adding dependencies for olvid module
try:
	import aiohttp
	tools_logger.debug("MonitoringBot: using aiohttp")
except ImportError:
	import urllib.request
	import urllib.error
	tools_logger.debug("MonitoringBot: using urllib")

from ..core.OlvidClient import OlvidClient
from ..core.OlvidBot import OlvidBot


class MonitoringBot(OlvidBot):
	# mandatory
	MONITORING_ENABLE_ENV_NAME = "MONITORING_ENABLE"
	MONITORING_SERVER_ENV_NAME = "MONITORING_SERVER"
	MONITORING_BOT_NAME_ENV_NAME = "MONITORING_BOT_NAME"
	# optional (at least one option must be set)
	MONITORING_MAIL_ADDRESSES_ENV_NAME = "MONITORING_MAIL_ADDRESSES"
	MONITORING_SMS_NUMBERS_ENV_NAME = "MONITORING_SMS_NUMBERS"
	MONITORING_WEBHOOK_URLS_ENV_NAME = "MONITORING_WEBHOOK_URLS"
	# optional
	# send a test notification on bot test (default to False)
	MONITORING_SEND_TEST_NOTIFICATION_ENV_NAME = "MONITORING_SEND_TEST_NOTIFICATION"
	# time in seconds between two test routine (default to 300 seconds)
	MONITORING_PERIOD_ENV_NAME = "MONITORING_PERIOD"

	def __init__(self, parent_client: OlvidClient = None, monitoring_routine: Callable[[Self], Union[bool, Coroutine[Any, Any, bool]]] = None):
		super().__init__(parent_client=parent_client)

		self.argument_monitoring_routine: Callable[[Self], Union[bool, Coroutine[Any, Any, bool]]] = monitoring_routine

		# init aiohttp session if using it
		self.aiohttp_session: Optional[aiohttp.ClientSession] = None
		if "aiohttp" in globals():
			self.aiohttp_session = aiohttp.ClientSession()

		# return None if monitoring is disabled
		self._monitoring_configuration: Optional[MonitoringBot.MonitoringConfiguration] = self._parse_env_config()
		if not self._monitoring_configuration:
			return

		if len(self._monitoring_configuration.sms_numbers) == 0 and len(self._monitoring_configuration.webhook_urls) == 0:
			tools_logger.warning(f"{self.name}: We do not recommend using mail alerts on it's own cause you have to check your mail box to validate your subscription on every start")

		subscribers_count = len(self._monitoring_configuration.sms_numbers) if self._monitoring_configuration.sms_numbers else 0
		subscribers_count += len(self._monitoring_configuration.mail_addresses) if self._monitoring_configuration.mail_addresses else 0
		subscribers_count += len(self._monitoring_configuration.webhook_urls) if self._monitoring_configuration.webhook_urls else 0
		tools_logger.info(f"{self.name}: enabled monitoring: {subscribers_count} alerts recipient set")

		# start monitoring
		self.add_background_task(self._start_monitoring_process(), f"{self.name}-initial-start-monitoring-task")

	async def stop(self):
		await super().stop()
		if self.aiohttp_session is not None:
			await self.aiohttp_session.close()

	#####
	# Interface (method to override)
	#####
	# override this method to execute code before calling refresh entry point
	# if this method fails, refresh will not be call and bot will be considered as down
	async def monitoring_routine(self):
		pass

	#####
	# Configuration parsing
	#####
	def _parse_env_config(self) -> Optional["MonitoringConfiguration"]:
		# check monitoring is enabled
		if not os.getenv(self.MONITORING_ENABLE_ENV_NAME, False):
			return None

		# check required config (server and bot name)
		server_url = os.getenv(self.MONITORING_SERVER_ENV_NAME, None)
		bot_name = os.getenv(self.MONITORING_BOT_NAME_ENV_NAME, None)
		if not server_url or not bot_name:
			raise self.MonitoringConfiguration.InvalidMonitoringConfigurationException(f"Monitoring server or bot name not specified")

		mail_addresses: list[str] = []
		if os.getenv(self.MONITORING_MAIL_ADDRESSES_ENV_NAME, ""):
			for mail_address in os.getenv(self.MONITORING_MAIL_ADDRESSES_ENV_NAME, "").split(","):
				if not mail_address:
					raise self.MonitoringConfiguration.InvalidMonitoringConfigurationException(f"Invalid mail address: {mail_address}")
				mail_addresses.append(mail_address)

		sms_numbers: list[str] = []
		if os.getenv(self.MONITORING_SMS_NUMBERS_ENV_NAME, ""):
			for sms_number in os.getenv(self.MONITORING_SMS_NUMBERS_ENV_NAME, "").split(","):
				if not sms_number:
					raise self.MonitoringConfiguration.InvalidMonitoringConfigurationException(f"Invalid mail address: {sms_number}")
				sms_numbers.append(sms_number)

		webhook_urls: list[str] = []
		if os.getenv(self.MONITORING_WEBHOOK_URLS_ENV_NAME, ""):
			for webhook_url in os.getenv(self.MONITORING_WEBHOOK_URLS_ENV_NAME, "").split(","):
				if not webhook_url:
					raise self.MonitoringConfiguration.InvalidMonitoringConfigurationException(f"Invalid webhook url: {webhook_url}")
				webhook_urls.append(webhook_url)

		if not mail_addresses and not sms_numbers and not webhook_urls:
			raise self.MonitoringConfiguration.InvalidMonitoringConfigurationException(f"No monitoring alert recipient specified")

		# get optional elements
		send_test_notification = os.getenv(self.MONITORING_SEND_TEST_NOTIFICATION_ENV_NAME, False)
		try:
			period = int(os.getenv(self.MONITORING_PERIOD_ENV_NAME, "300"))
		except ValueError:
			raise self.MonitoringConfiguration.InvalidMonitoringConfigurationException(f"Monitoring period is not a valid int")
		if period < 60:
			raise self.MonitoringConfiguration.InvalidMonitoringConfigurationException(f"Monitoring period cannot be smaller than 60 seconds")

		return self.MonitoringConfiguration(
			server_url=server_url,
			bot_name=bot_name,
			period=period,
			mail_addresses=mail_addresses,
			sms_numbers=sms_numbers,
			webhook_urls=webhook_urls,
			send_test_notification=send_test_notification
		)

	#####
	# Monitoring routine core
	#####
	async def _start_monitoring_process(self):
		tools_logger.debug("monitoring: starting process")
		# build request payload
		json_payload = {
			"bot_name": self._monitoring_configuration.bot_name,
			"duration_before_alert": 2 * self._monitoring_configuration.period,  # bot have two periods to
			"alerts": []
		}

		if len(self._monitoring_configuration.mail_addresses):
			json_payload["alerts"].append({"type": "mail", "recipients": self._monitoring_configuration.mail_addresses})
		if len(self._monitoring_configuration.sms_numbers):
			json_payload["alerts"].append({"type": "sms", "recipients": self._monitoring_configuration.sms_numbers})
		if len(self._monitoring_configuration.webhook_urls):
			json_payload["alerts"].append({"type": "webhook", "recipients": self._monitoring_configuration.webhook_urls})

		# register on server
		try:
			status, body = await self.async_http_request(self._monitoring_configuration.server_url + "/register", "POST", json.dumps(json_payload))
			if status != 200:
				raise RuntimeError(f"Unable to subscribe to monitoring: {status}: {body}")
			subscription_id: str = body
		except Exception as e:
			tools_logger.exception(f"{self.name}: exception during subscription process: {e} ({json_payload})")
			raise e

		# send test notification if necessary
		if self._monitoring_configuration.send_test_notification:
			try:
				status, body = await self.async_http_request(url=self._monitoring_configuration.server_url + "/test", method="POST", payload=subscription_id)
				if status != 200:
					raise RuntimeError(f"An error occurred when sent test notification: {status}: {body}")
			except Exception as e:
				tools_logger.exception(f"monitoring: exception when sending test message: {e} ({subscription_id})")
				raise e

		# add a background task to refresh subscription on monitoring server
		async def refresh_subscription_task():
			while True:
				try:
					# execute arbitrary code before refreshing subscription on server
					res = self.monitoring_routine()
					if iscoroutine(res):
						await res
					if self.argument_monitoring_routine:
						res = self.argument_monitoring_routine(self)
						if iscoroutine(res):
							await res

					# refresh subscription on server
					refresh_status, refresh_body = await self.async_http_request(url=self._monitoring_configuration.server_url + "/refresh", method="POST", payload=subscription_id)

					# subscription expired on server, launch a new subscription process in background and end this task
					if refresh_status == 404:
						tools_logger.error(f"{self.name}: refresh: server returned a 404 error, restarting monitoring process")
						self.add_background_task(self._start_monitoring_process())
						return

					if refresh_status != 200:
						raise Exception(f"Server returned an error: {refresh_status}")

					tools_logger.debug(f"{self.name}: pinged monitoring server")
					await asyncio.sleep(self._monitoring_configuration.period)

				except Exception:
					# an error occurred try to refresh faster before subscription expiration
					tools_logger.exception(f"{self.name}: an error occurred during refresh process ({subscription_id})")
					await asyncio.sleep(5)

		# start task if running, else wait for client start (avoid asyncio loop issues)
		self.add_background_task(refresh_subscription_task(), "monitoring-refresh-task")

	####
	# Http methods (we use aiohttp if available, else we run urllib in executor)
	# This returns a tuple with http response status and body
	####
	async def async_http_request(self, url: str, method: str, payload: str = None) -> tuple[int, str]:
		if "aiohttp" in globals():
			async with self.aiohttp_session.request(method=method, url=url, data=payload) as response:
				return response.status, await response.text()
		else:
			def sync_http_request() -> tuple[int, str]:
				try:
					with urllib.request.urlopen(urllib.request.Request(url=url, method=method, data=payload.encode() if payload else None)) as resp:
						return (resp.status, resp.read())
				except urllib.error.HTTPError as error:
					return (error.status, error.read().decode())
			return await asyncio.get_event_loop().run_in_executor(None, sync_http_request)

	class MonitoringConfiguration():
		def __init__(
				self,
				server_url: str,
				bot_name: str,
				period: int = 120,
				mail_addresses: list[str] = (),
				sms_numbers: list[str] = (),
				webhook_urls: list[str] = (),
				send_test_notification: bool = False

		):
			self.server_url: str = server_url
			self.bot_name: str = bot_name
			self.period: int = period
			self.mail_addresses: list[str] = mail_addresses
			self.sms_numbers: list[str] = sms_numbers
			self.webhook_urls: list[str] = webhook_urls
			self.send_test_notification: bool = send_test_notification

		class InvalidMonitoringConfigurationException(Exception):
			pass
