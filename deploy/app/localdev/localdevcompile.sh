#!/bin/bash
echo "============================================================"
echo "Running local dev compile file..."
python3 manage.py wait_for_db
python3 manage.py migrate
echo "Loading data..."
python3 manage.py loaddata user.json
python3 manage.py loaddata city_info.json

# python3 manage.py loaddata sample.json

echo "Start server..."
python3 manage.py runserver 0.0.0.0:8000 --insecure
