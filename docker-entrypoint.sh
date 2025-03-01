#!/bin/bash

# Wait for database
echo "Waiting for database..."
sleep 5

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --settings=shelter.settings.base_settings

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn shelter.wsgi:application --bind 0.0.0.0:8000 --workers 3 