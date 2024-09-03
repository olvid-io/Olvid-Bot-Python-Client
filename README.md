# Olvid Bot Python Client

# Introduction
This repository is part of the Olvid bots framework. If you are lost you might start here: [Quickstart](https://github.com/olvid-io/Olvid-Bot-Quickstart)

Note that the usage of this framework is part of Olvid's paying features. You can use this repository to deploy and test framework possibilities, but if you want to use it without limitations, please contact the Olvid team at bot@olvid.io.

# Install
You can install this module using pip. Using pypi repository:
```bash
pip3 install olvid-bot 
```
Or from source:
```bash
git clone https://github.com/olvid-io/Olvid-Bot-Python-Client
cd Olvid-Bot-Python-Client
pip3 install .
```

# Python Client
### Terminology
- Daemon: a standalone and fully manageable Olvid application exposing gRPC services to control it.
- Bot/Client: Any program that interacts with a daemon instance on behalf of a user.
- CLI (Command-Line Interface): A text-based interface to setup and manually interact with a daemon instance. (included in this module)
- Identity: An Olvid profile hosted in a daemon.
- Client Key: A unique identifier used to authenticate with the Olvid API. A client key is associated with an identity and only gives client rights to manage this identity.
- API Key: A key given by Olvid team to let you use this framework without limitations. This key is set up once.

### Introduction
This module implements a gRPC client and aims to add features to make it as straightforward as possible, while still providing complete access to all features for achieving the most advanced tasks.

The module embed a CLI (Command Line Interface) to let you manually interact with Daemon.
See [README-cli](./README-cli.md).

### Organization
#### Daemon API
In the Daemon API, each gRPC service (within the API) can be associated with two key aspects: its type and its entity.

There are three types of services:
- Command: Methods in such a service allow for retrieving data, modifying it, executing actions, and more.
- Admin: Similar to a command service, but accessible only with an admin client_key that has administrative privileges.
- Notification: Enables registration for a specific notification type and receives a message whenever the corresponding event occurs.

An entity is a logical element within Olvid. Examples of entities include Identity, Message, Discussion, and more.
You can link most of these entities to elements in your Olvid application: an identity is the profile you created when you started using Olvid and a discussion regroup messages you exchanged with a contact or within a group. 

Following the model of services defined by their type and entity, we can find services like MessageCommandService and MessageNotificationService. 
These services implement methods such as messageSend to send a message and messageReceived to receive notifications for each new incoming message.

We also have services like IdentityAdminService and IdentityCommandService.
With the first one you can create or delete identities, provided you have admin permissions, while the latter gives you access to your current identity and to edition methods (e.g., adding a photo, edit you name, ...).

Here is the repository with the full [daemon API specifications](https://github.com/olvid-io/Olvid-Bot-Protobuf)

#### OlvidClient
[OlvidClient](./olvid/core/OlvidClient.py) implements every gRPC command methods defined in daemon API.
You can find methods using the same name as in gRPC but using snake case.
Request and Response encapsulation layer is fully invisible, you won't need to use Request and Response messages.
For example for message_send method you can use:
`client.message_send(discussion_id, body)` and it will return a `datatypes.Message` item.
you don't use MessageSendRequest and MessageSendResponse.

OlvidClient also implements a Listener mechanism to listen to notification implemented in grpc Notification services.
Use this code to add a listener to message_received notification:
`client.add_listener(listeners.MessageReceivedListener(handler=lambda message: print(message)))`
Again you won't need to use encapsulation messages SubscribeToMessageSendNotification and MessageReceivedNotification.

### OlvidBot
[OlvidBot](./olvid/core/OlvidBot.py): extends OlvidClient to add notification handlers.

As OlvidBot extends OlvidClient it has the same constraints, for example it needs to find a valid client_key to
connect to a daemon (see [Authentication](#authentication)).

OlvidBot implements a set of method named on_something. There is one method for each gRPC notification method.
On instantiation overwritten methods will automatically be subscribed as notification listener.
For example:
```
class Bot(OlvidBot)
    async def on_message_received(self, message: datatypes.Message):
        print(message)
```
Every time Bot class is instantiated it will add a listener to message_received notification with the method as handler.

OlvidBot can also add [Command](./olvid/listeners/Command.py) objects with add_command method. Command are specific listeners.
They subclass listeners.MessageReceivedListener, and they are created with a regexp filter that will filter notifications.
Only messages that match the regexp will raise a notification.
Commands can be added using OlvidBot.command decorator:
For example:
```
class Bot(OlvidBot)
    OlvidBot.command(regexp_filter="^!help")
    async def on_message_received(self, message: datatypes.Message):
        await message.reply("Help message")
```

### Authentication
OlvidClient needs a client key to authenticate on daemon, you can pass it using:
- by setting OLVID_CLIENT_KEY env variable
- by writing it in a .client_key file
- by passing it as a client_key constructor parameter (to avoid)

By default, client connects to "localhost:50051" you can change this behavior:
- set DAEMON_HOSTNAME and/or DAEMON_PORT env variable
- use server_target parameter. It must be the full server address including hostname/ip and port

An [OlvidAdminClient](./olvid/core/OlvidAdminClient.py) use the same mechanism but because it needs an admin client key
it use the OLVID_ADMIN_CLIENT_KEY env variable and the .admin_client_key file to find a key to use.

#### Concepts
- **Listener**: a listener is a class that implements a method that will be called when a notification is received. [GenericNotificationListener.py](./olvid/listeners/GenericNotificationListener.py).
You can add listeners to any OlvidClient subclass.
We do not recommend that you use GenericNotificationListener directly. Instead, you should use one of the provided
listeners in the ListenersImplementation file.
You can access them like this:
```
from olvid import listeners
listeners.MessageReceivedListener(handler=lambda m: a)
```
Like this you won't need to specify the notification you want to listen to.
Also, you won't need to use protobuf Notification messages, message are already un-wrapped and handler ill receive notification content.
For example MessageReceivedListener.handler will receive a datatypes.Message item, not a MessageReceivedNotification
as a GenericNotificationListener will receive if listening to MessageReceivedNotification.

- **Command**: a (Command)[./olvid/core/Command.py] is a specific MessageReceivedListener associated with a regexp that will determine if it's called or not.
The most convenient way to add a command is to use the `OlvidBot.command` decorator, like this command are automatically
added to an OlvidBot instance.
Examples of possible way to add commands to a bot:

```
class Bot(OlvidBot):
    # use decorator in you bot class declaration
    @OlvidBot.command(regexp_filter="^!help")
    async def help_cmd(self, message: datatypes.Message):
        await message.reply("help message")

bot = OlvidBot()

# use decorator to to an existing bot instance
@bot.command(regexp_filter="!second")
async def second_command(message: datatypes.Message):
    print("Second command")

# use add_command method
bot.add_command(Command(regexp_filter="^!cmd", handler=lambda message: print(message)))
```
