import asyncio
import inspect
import json
from abc import ABC, abstractmethod
from asyncio import Task
from datetime import datetime
from typing import Optional, Coroutine

from olvid import OlvidClient

from .logger import tools_logger


# the class that will manage tasks have to extend this class.
# - storage_prefix: must be unique for every task holder.
#   this prefix allows holder to recognize its fields in the database.
# Initialization: actually self.load method is called asynchronously, in the background.
# so this class might not be initialized on the instance creation.
# if you need to know when it's initialized, you can check self._tasks_map is not None.
# if you need to force initialization, you can call self.load by yourself
class DelayedTasksHolder:
	# override this abstract class to use the DelayedTaskHolder
	# Instances will be json serialized, so you must store necessary data in the dict returned by serialize method.
	# - discussion_id is a very important attribute if you are creating tasks associated with a discussion,
	# 	and you want these tasks to be still associated with this discussion after a backup restoration.
	#   if you don't use discussion, you can set discussion_id to 0 all the time
	# - task_id must be unique.
	# if you need to update / delete your tasks, you will need to guess this id.
	# in that case, most of the time,
	#   use the message_id that created this task.
	#   if you don't need to retrieve your task later this id can be anything random.
	class DelayedTask(ABC):
		@abstractmethod
		def get_execution_timestamp(self) -> int:
			pass

		@abstractmethod
		def get_task_id(self) -> str:
			pass

		@abstractmethod
		def get_discussion_id(self) -> Optional[int]:
			pass

		@abstractmethod
		def is_repeated(self) -> bool:
			pass

		@abstractmethod
		def serialize(self) -> dict:
			pass

		@staticmethod
		@abstractmethod
		def deserialize(serialized_dict: dict) -> "DelayedTasksHolder.DelayedTask":
			pass

		@abstractmethod
		async def run(self, client: OlvidClient):
			pass

	# Storage_prefix must be a unique and constant string.
	# It's used to determine if an element in storage is associated with a specific task holder.
	def __init__(self, client: OlvidClient, task_class: type[DelayedTask], storage_prefix: str):
		# we use olvid client to access storage, and we pass it to tasks on execution.
		self._client: OlvidClient = client
		# we use a unique storage prefix to easily determine tasks associated with a task holder in daemon storage.
		# this prefix must be uniquely associated with a task holder class.
		self._storage_prefix: str = storage_prefix
		# We need task class to deserialize tasks
		self._task_class: type[DelayedTasksHolder.DelayedTask] = task_class

		# we keep in memory a copy of storage state to make next timer computation easier.
		# this map is set to None until load method is called and initialize it
		self._tasks_map: Optional[dict[str, DelayedTasksHolder.DelayedTask]] = None

		# store current timer task (task waiting for the next execution and that will execute passed events handlers)
		self._timer_task: Optional[asyncio.Task] = None
		# store a datetime object holding the next timer_task expiration
		self._current_timer_execution_timestamp: Optional[int] = None
		# A set of all background tasks.
		# We use it to execute tasks in the background.
		# Tasks are automatically removed when executed.
		self.__task_set = set()

		# load registered tasks lazily because we must do asyncio calls (the task map will be None until the loading end)
		self._add_background_task(self.load(), f"{self.__class__.__name__}-load-on-start")

	# load previous tasks
	async def load(self):
		if self._tasks_map is not None:
			return
		# this instance has already been initialized
		self._tasks_map = {}
		# load global tasks
		async for element in self._client.storage_list():
			if self._is_valid_task_storage_key(key=element.key):
				try:
					task = self._task_class.deserialize(json.loads(element.value))
					self._tasks_map[task.get_task_id()] = task
					tools_logger.info(f"Loaded task: {task.get_task_id()}: {task.get_execution_timestamp()}")
				except json.JSONDecodeError:
					tools_logger.exception(f"{self.__class__.__name__}: list_tasks: discussion ({0}): cannot decode element in storage with key: {element.key}")
					continue

		# load discussion tasks
		async for discussion in self._client.discussion_list():
			async for element in self._client.discussion_storage_list(discussion_id=discussion.id):
				if element.key.startswith(self._storage_prefix):
					try:
						task = self._task_class.deserialize(json.loads(element.value))
						self._tasks_map[task.get_task_id()] = task
						tools_logger.info(f"Loaded task: {task.get_task_id()}: {task.get_execution_timestamp()}")
					except Exception:
						tools_logger.exception(f"{self.__class__.__name__}: list_tasks: discussion ({discussion.id}): cannot decode element in storage with key: {element.key}")

		self._refresh_timer()

	####
	# Public Api
	####
	# set discussion_id to 0 if you want to list tasks not associated to a discussion
	async def list_tasks(self, discussion_id: int) -> list["DelayedTasksHolder.DelayedTask"]:
		return [task for task in self._tasks_map.values() if task.get_discussion_id() == discussion_id]

	# set discussion_id to 0 if you want to get a task not associated to a discussion
	async def get_task(self, task_id: str, discussion_id: int) -> Optional["DelayedTasksHolder.DelayedTask"]:
		task = self._tasks_map.get(task_id)
		return None if not task else task if task.get_discussion_id() == discussion_id else None

	async def add_task(self, task: "DelayedTasksHolder.DelayedTask"):
		# update storage
		task_storage_key = self._get_task_storage_key(task.get_task_id())
		if not task.get_discussion_id():
			await self._client.storage_set(key=task_storage_key, value=json.dumps(task.serialize()))
		else:
			await self._client.discussion_storage_set(discussion_id=task.get_discussion_id(), key=task_storage_key, value=json.dumps(task.serialize()))

		# update task map
		self._tasks_map[task.get_task_id()] = task

		# refresh timer
		self._refresh_timer()

	async def remove_task(self, task: "DelayedTasksHolder.DelayedTask"):
		# update storage
		if task.get_discussion_id() == 0:
			await self._client.storage_unset(key=self._get_task_storage_key(task.get_task_id()))
		else:
			await self._client.discussion_storage_unset(discussion_id=task.get_discussion_id(), key=self._get_task_storage_key(task.get_task_id()))

		# update task map
		self._tasks_map.pop(task.get_task_id())

		# refresh timer
		self._refresh_timer()

	async def update_task(self, updated_task: "DelayedTasksHolder.DelayedTask"):
		# update storage
		task_storage_key = self._get_task_storage_key(updated_task.get_task_id())
		if updated_task.get_discussion_id() == 0:
			await self._client.storage_set(key=task_storage_key, value=json.dumps(updated_task.serialize()))
		else:
			await self._client.discussion_storage_set(discussion_id=updated_task.get_discussion_id(), key=task_storage_key, value=json.dumps(updated_task.serialize()))

		# update task map
		self._tasks_map[updated_task.get_task_id()] = updated_task

		# refresh timer
		self._refresh_timer()

	####
	# Timer api
	####
	def _refresh_timer(self):
		try:
			# no more tasks to handle
			if len(self._tasks_map) == 0:
				if self._timer_task:
					self._timer_task.cancel()
					self._timer_task = None
				return

			# determine next task to execute
			next_task: Optional[DelayedTasksHolder.DelayedTask] = None
			next_execution: int = self._current_timer_execution_timestamp
			for task in self._tasks_map.values():
				if next_execution is None:
					next_execution = task.get_execution_timestamp()
					next_task = task
				elif task.get_execution_timestamp() < next_execution:
					next_execution = task.get_execution_timestamp()
					next_task = task

			# if next handler is set this means that timer delay changed and it must be updated
			if next_task is not None:
				# stop previous background timer task
				if self._timer_task:
					self._timer_task.cancel()

				# setup timer
				delay_s = next_execution - datetime.now().timestamp()
				# if delay is negative, some tasks require to be executed now (timer_task will re-sync timer)
				if delay_s < 0:
					self._timer_task = self._add_background_task(self._timer_task_method(0), name=f"{self.__class__.__name__}-timer-task")
					return
				# else setup a timer
				self._timer_task = self._add_background_task(self._timer_task_method(delay_s), name=f"{self.__class__.__name__}-timer-task")
				self._current_timer_execution_timestamp = next_execution
		except Exception:
			tools_logger.exception("Unexpected exception in _refresh_timer")

	async def _timer_task_method(self, delay_s: float):		# await for delay
		try:
			if delay_s > 0:
				await asyncio.sleep(delay_s)

			# executed expired tasks
			tasks_to_remove: list[DelayedTasksHolder.DelayedTask] = []
			now = datetime.now()

			for task_id, task in self._tasks_map.items():
				try:
					if task.get_execution_timestamp() <= now.timestamp():
						ret = task.run(self._client)
						if inspect.iscoroutine(ret):
							self._add_background_task(ret, name=f"{self.__class__.__name__}-{task_id}")
						tasks_to_remove.append(task)
				except Exception:
					tools_logger.exception(f"{self.__class__.__name__}: _timer_task_method: an error occurred when running a task: {task_id}")

			# if ran tasks are not repeated, we can delete them
			for task in tasks_to_remove:
				if task.is_repeated():
					# update task in memory to update next execution timestamp
					await self.update_task(task)
				else:
					await self.remove_task(task)

			# reset timer delay
			self._current_timer_execution_timestamp = None

			# relaunch timer
			self._refresh_timer()
		except asyncio.CancelledError:
			raise
		except Exception:
			tools_logger.exception("Unexpected exception in _time_task_method")

	####
	# Internal
	####
	def _get_task_storage_key(self, task_id: str) -> str:
		return f"{self._storage_prefix}{task_id}"

	def _is_valid_task_storage_key(self, key: str) -> bool:
		return key.startswith(self._storage_prefix) and len(key) > len(self._storage_prefix)

	def _add_background_task(self, coroutine: Coroutine, name: str = "") -> Task:
		task = asyncio.get_event_loop().create_task(coroutine, name=name if name else None)
		self.__task_set.add(task)

		def end_callback(t):
			self.__task_set.remove(t)
		task.add_done_callback(end_callback)
		return task
