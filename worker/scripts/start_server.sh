#!/bin/bash
VENV="/home/ubuntu/server/venv/"
ACTIVATE="${VENV}bin/activate"
source "$ACTIVATE"

DIR="/home/ubuntu/worker/"
APP="wsgi:app"
ADDRESS="0.0.0.0:80"
gunicorn --chdir $DIR  --bind $ADDRESS $APP