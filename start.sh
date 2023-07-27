#!/bin/bash


python manage.py migrate

gunicorn -b :8080 --workers 1 --threads 8 main.wsgi:application