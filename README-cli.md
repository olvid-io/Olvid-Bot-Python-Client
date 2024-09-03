# Olvid Bot Command Line Interface

## Install
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
