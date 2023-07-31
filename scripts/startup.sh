#!/bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py spectacular --color --file schema.yml

gunicorn -b :8080 --workers 1 --threads 8 main.wsgi:application