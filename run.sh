#!/bin/bash

. ${HOME}/venv/bin/activate

cd ${HOME}/sigsis
python manage.py runserver
