#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="/etc/confidant/firebase-service-account.json"
env FLASK_APP=app.py flask run -h 0.0.0.0 -p 5000