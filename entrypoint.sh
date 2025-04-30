#!/bin/bash

# Wait for DB (optional)
# echo "Waiting for database..."
# sleep 10

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting uWSGI..."
uwsgi --ini uwsgi.ini
