#!/bin/bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install curl -y
sudo apt install wget -y
sudo apt install net-tools -y
sudo apt install strace -y
sudo apt install iftop -y
sudo apt install lsof -y
sudo apt install chkrootkit -y
sudo apt install inxi -y
sudo apt install lshw -y
wget https://raw.githubusercontent.com/dylan14567/configserver/main/configserver.py
wget https://raw.githubusercontent.com/dylan14567/configserver/main/requirements.txt
chmod +x configserver.py
pip install -r requirements.txt
