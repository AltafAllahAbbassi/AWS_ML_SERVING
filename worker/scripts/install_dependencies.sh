#!/bin/bash

VENV="/home/ubuntu/server/venv/"
ACTIVATE="${VENV}bin/activate"

sudo apt update -y
sudo apt install python3-pip -y
pip install --upgrade pip
sudo apt install python3-venv -y
python3 -m venv $VENV
source "$ACTIVATE"
pip3 install Flask
pip3 install gunicorn
pip3 install requests
pip3 install setuptools-rust
pip3 install transformers
pip3 install torch 
deactivate



