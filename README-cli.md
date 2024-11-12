# Olvid Bot Command Line Interface

## Introduction
Welcome to the Olvid Python Client repository, part of the Olvid bots framework. 
If you're new here, consider starting with our [Documentation](https://doc.bot.olvid.io).

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

To start cli in interactive mode use
```bash
olvid-cli
```
or
```bash
python3 -m olvid
```

## Global behaviour
At any time use `--help` flag to get information on a command.
For example use
```
identity --help
```
To see available commands related to daemon identities.
And use 
```
identity new --help
```
To see how to use `identity new` command
