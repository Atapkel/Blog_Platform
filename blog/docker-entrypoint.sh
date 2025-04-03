#!/bin/bash
set -e

until pg_isready -h db -U bloguser -d blogdb; do
    echo "Waiting for database..."
    sleep 2
done

python manage.py migrate
python manage.py runserver 0.0.0.0:8000