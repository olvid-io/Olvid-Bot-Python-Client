# **Olvid Bot Python Client**

## Introduction
Welcome to the Olvid Python Client repository, part of the Olvid bots framework. If you're new here, consider starting with our [Quickstart guide](https://github.com/olvid-io/Olvid-Bot-Quickstart).

**Note**: The use of this framework is a paying feature. You can use this repository to deploy and test the framework's possibilities, but if you want to use it without limitations, please contact the Olvid team at [bot@olvid.io](mailto:bot@olvid.io).

## Installation

You can install this module using pip:

```bash
pip3 install olvid-bot
```

Or from source:

```bash
git clone https://github.com/olvid-io/Olvid-Bot-Python-Client
cd Olvid-Bot-Python-Client
pip3 install .
```

## Overview

This Python module implements a robust gRPC client, designed to simplify interactions while providing complete access to every RPC.
This allows you to achieve advanced tasks with ease.
To see the complete gRPC and protobuf description of the Daemon API, please refer to the [protobuf repository](https://github.com/olvid-io/Olvid-Bot-Protobuf).

The module also includes a built-in **CLI (Command-Line Interface)**, enabling manual interaction with the Daemon for efficient management and testing.
For more information on using the CLI, refer to [README-cli](./README-cli.md).

## Terminology

* **Daemon**: a self-contained, fully manageable Olvid application that exposes gRPC services for control and interaction.
* **Bot/Client**: any program that interacts with a daemon instance on behalf of a user, facilitating communication and task execution.
* **CLI (Command-Line Interface)**: a text-based interface for setting up and manually interacting with a daemon instance, included in this module for easy access and management.
* **Identity**: an Olvid profile hosted within a daemon, representing a unique user entity.
* **Client Key**: a unique identifier used to authenticate with the Olvid API, associated with an identity and granting client rights to manage that identity.
* **API Key**: a special key provided by the Olvid team, enabling unrestricted use of the framework; set up once for convenient access.

## Code
### OlvidClient
#### Authentication
To authenticate with the daemon, OlvidClient requires a client key. You can provide this key by:

* Setting the `OLVID_CLIENT_KEY` environment variable
* Writing it to a `.client_key` file
* Passing it as a `client_key` constructor parameter (not recommended)

Most of the time the client key is generated with `identity new` CLI command.
You can retrieve it or manage your client key using `key` command group in CLI.

#### Daemon address
By default, the client connects to `"localhost:50051"`. You can modify this behavior by:

* Setting `DAEMON_HOSTNAME` and/or `DAEMON_PORT` environment variables
* Using the `server_target` parameter with the full server address (including hostname/IP and port)

An [OlvidAdminClient](./olvid/core/OlvidAdminClient.py) uses a similar mechanism, but requires an admin client key. It utilizes the `OLVID_ADMIN_CLIENT_KEY` environment variable and the `.admin_client_key` file to find a key.

#### Command API

The [OlvidClient](./olvid/core/OlvidClient.py) class provides a convenient interface to interact with the daemon API, implementing every command services RPC.
You can find method associated to a RPC in an OlvidClient instance as methods using snake case naming conventions.
You will also find correlations between method parameters and RPC request messages, and method return values and RPC response messages.

Here is an example RPC description:
```protobuf
message MessageGetRequest {
  datatypes.v1.MessageId message_id = 1;
}
message MessageGetResponse {
  datatypes.v1.Message message = 1;
}
service MessageCommandService {
  rpc MessageGet(command.v1.MessageGetRequest) returns (command.v1.MessageGetResponse) {}
}
```

In OlvidClient you will find this method prototype
```python
async def message_get(self, message_id: datatypes.MessageId) -> datatypes.Message
```
As you can see you there is one mandatory parameter for `message_id` and it returns a `Message` object

#### Listeners
OlvidClient also features a Listener mechanism to handle notifications implemented in the gRPC Notification services.
There is an generic class named [GenericNotificationListener](./olvid/listeners/GenericNotificationListener.py) describing Listeners principle.

There is an implementation of this class for each kind of notification in [ListenersImplementation](./olvid/listeners/ListenersImplementation.py)

To add a basic listener and execute a method every time a message arrives you can add a MessageReceivedListener.

This code will run forever and print every new message.
```python
import asyncio
from olvid import OlvidClient, listeners

async def main():
    client = OlvidClient()
    client.add_listener(listeners.MessageReceivedListener(handler=lambda message: print(message)))
    await client.wait_for_listeners_end()

asyncio.run(main())
```

### OlvidBot
#### Notification handlers
The [OlvidBot](./olvid/core/OlvidBot.py) class extends OlvidClient, adding notification handlers for a more comprehensive experience.
As it builds upon OlvidClient, it inherits the same constraints, such as requiring a valid client_key to connect to a daemon (see [Authentication](#authentication)).
But it also brings all the method to call Daemon commands.

OlvidBot introduces methods prefixed with `on_`, one for each gRPC notification method.
When you instantiate an OlvidBot subclass, overridden methods will automatically be subscribed as notification listeners.

This code will run forever and print every new message content.
```python
import asyncio
from olvid import OlvidBot, datatypes

class Bot(OlvidBot):
    async def on_message_received(self, message: datatypes.Message):
        print(message.body)

async def main():
    bot = Bot()
    await bot.wait_for_listeners_end()

asyncio.run(main())
```
#### Command listeners
OlvidBot also supports adding [Command](./olvid/listeners/Command.py) objects using the `add_command` method.
Commands are specific `listeners.MessageReceivedListener` sub-classes. 
They are created with a regexp filter to selectively trigger notifications.

You can add commands using the `OlvidBot.command` decorator:

```python
from olvid import OlvidBot, datatypes

class Bot(OlvidBot):
    @OlvidBot.command(regexp_filter="^!help")
    async def on_message_received(self, message: datatypes.Message):
        await message.reply("Help message")

async def main():
    bot = Bot()
    await bot.wait_for_listeners_end()
```

Or you can also dynamically define and add a command to a bot instance.
```python
from olvid import OlvidBot, datatypes, listeners

async def main():
    bot = OlvidBot()
    bot.add_command(listeners.Command(
        regexp_filter="!help",
        handler=lambda m: print("Help as been requested")
    ))
    await bot.wait_for_listeners_end()
```
