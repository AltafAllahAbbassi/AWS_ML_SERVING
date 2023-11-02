#!/bin/bash

VENV="/home/ubuntu/server/venv/"
ACTIVATE="${VENV}bin/activate"

sudo apt update -y
sudo apt install python3-pip -y
sudo apt install python3-venv -y
python3 -m venv $VENV
source "$ACTIVATE"
pip3 install flask
pip3 install gunicorn
pip3 install requests
deactivate

