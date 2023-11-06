#!/bin/bash

set -e

# navigate to project root directory
pushd "$APP_HOME" > /dev/null

# Apply migrations
python manage.py migrate

# Start server
if [ "$DJANGO_ENV" == "local" ]; then
    python \
        -Xfrozen_modules=off \
        -m debugpy --listen 0.0.0.0:${DEBUGPY_PORT} \
        manage.py runserver ${HOST}:${PORT} \
        --insecure \
        --nostatic
else
    gunicorn --workers=1 --bind=${HOST}:${PORT} --chdir=/app django_vue_experiments.wsgi:application
fi
