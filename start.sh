#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput --username admin --email admin@example.com || echo "Superuser already exists"
gunicorn bezbreda.wsgi:application --bind 0.0.0.0:$PORT