#!/bin/bash

sudo export GOOGLE_APPLICATION_CREDENTIALS="/etc/confidant/firebase-service-account.json"
sudo env FLASK_APP=app.py flask run -h 0.0.0.0 -p 443