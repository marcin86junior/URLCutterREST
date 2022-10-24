#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

echo "Test website"
python manage.py test
coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
coverage report

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000