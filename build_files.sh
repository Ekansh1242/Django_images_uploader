#!/bin/bash
set -e
set -x

echo "Installing dependencies..."
pip install --break-system-packages -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Verifying staticfiles directory..."
ls -la staticfiles

echo "Applying migrations..."
python manage.py migrate --noinput