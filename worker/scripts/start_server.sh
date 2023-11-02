#!/bin/bash

DIR="/home/ubuntu/worker/"
GUNICORN="${DIR}venv/bin/gunicorn"
APP="wsgi:app"
ADDRESS="0.0.0.0:80"

sudo "$GUNICORN" --chdir $DIR  --bind $ADDRESS $APP