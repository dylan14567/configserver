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
sudo apt install git -y
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install build-essential libssl-dev libffi-dev python3-dev -y
git clone https://github.com/dylan14567/configserver
cd configserver
chmod +x *;ls
pip install -r requirements.txt
python3 setup.py install
cd
rm -rf install.sh
