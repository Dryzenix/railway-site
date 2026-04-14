#!/bin/bash
set -e

echo "Starting migrations..."
python manage.py migrate
echo "Migrations done"

echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Static files collected"

echo "Creating superuser..."
python manage.py createsuperuser --noinput --username admin --email admin@example.com || echo "Superuser already exists"
echo "Superuser done"

echo "Starting gunicorn..."
gunicorn bezbreda.wsgi:application --bind 0.0.0.0:$PORT