#!/bin/sh

set -e

# Wait for PostgreSQL using psql
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

echo "Applying migrations..."
python manage.py migrate

exec "$@"