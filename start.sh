#!/bin/bash


python manage.py migrate

python manage.py collectstatic

gunicorn -b :8080 --workers 1 --threads 8 main.wsgi:application