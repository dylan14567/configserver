# configserver
[![Build Status](https://img.shields.io/github/stars/dylan14567/configserver.svg)](https://github.com/dylan14567/configserver)
[![License](https://img.shields.io/github/license/dylan14567/configserver.svg)](https://github.com/dylan14567/configserver/blob/main/LICENSE)
[![dylan14567](https://img.shields.io/badge/author-dylan14567-green.svg)](https://github.com/dylan14567)
[![bug_report](https://img.shields.io/badge/bug-report-red.svg)](https://github.com/dylan14567/configserver/blob/main/.github/ISSUE_TEMPLATE/bug_report.md)
[![security_policy](https://img.shields.io/badge/security-policy-cyan.svg)](https://github.com/dylan14567/configserver/blob/main/SECURITY.md)
[![Python](https://img.shields.io/badge/language-Python%20-yellow.svg)](https://www.python.org)

Configure your linux server and check for vulnerabilities with configserver.

Configserver has a menu with options and allows you to configure your server through that menu but you can also import the configserver module in another file.

## Pre-requirements

The requirements to use the system is to have the following python modules installed:

```
colorama
requests
wheel
```

## Installation

To install configserver on linux run these commands on your Linux Terminal.

```shell

pip install configserver

```

Once done, it begins to install.

to start configserver you just have to put the ``` configserver ``` command in the terminal.

Ready

## Usage:

To use the configserver command you just have to put the ```configserver``` command, and once that is done the system menu will be loaded.

## Custom script

If you want to create your own menu and your own code using the configserver module you must do the following:

```python 

from adminserver.main import *

server = server ()

server.systeminfo () # Shows you system information
server.listusers () # List system users
server.installpackages () # install the apt packages necessary for the code to work
server.addnewuser () # Add new users

# Removing information from my website
link = "127.0.0.1"
server.header (link) # Get information from a website

```

## Authors

* **Dylan Alexander** - *Initial Work* - [dylan14567](https://github.com/dylan14567)

You can also look at the list of all [contributors](https://github.com/dylan14567/configserver/contributors) who have participated in this project.

## License

The license for this project is <a href="https://github.com/dylan14567/configserver/blob/main/LICENSE">MIT </a>
