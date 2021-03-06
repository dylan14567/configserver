# configserver
[![Build Status](https://img.shields.io/github/stars/dylan14567/configserver.svg)](https://github.com/dylan14567/configserver)
[![License](https://img.shields.io/github/license/dylan14567/configserver.svg)](https://github.com/dylan14567/configserver/blob/main/LICENSE)
[![dylan14567](https://img.shields.io/badge/author-dylan14567-green.svg)](https://github.com/dylan14567)
[![bug_report](https://img.shields.io/badge/bug-report-red.svg)](https://github.com/dylan14567/configserver/blob/main/.github/ISSUE_TEMPLATE/bug_report.md)
[![security_policy](https://img.shields.io/badge/security-policy-cyan.svg)](https://github.com/dylan14567/configserver/blob/main/SECURITY.md)
[![Bash](https://img.shields.io/badge/language-Bash-blue.svg)](https://www.gnu.org/software/bash/)
[![Python](https://img.shields.io/badge/language-Python%20-yellow.svg)](https://www.python.org)

Configserver is a system created by dylan14567, and this system helps you manage your ubuntu server.

## Installation

To install configserver on linux run these commands on your Linux Terminal.

```shell

pip install configserver

```

Once done, it begins to install.

Ready

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
## License

The license for this project is <a href="https://github.com/dylan14567/configserver/blob/main/LICENSE">MIT </a>
