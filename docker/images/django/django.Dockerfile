# ---------------------
# Base
# ---------------------
FROM python:3.11-slim-bullseye as base

# Build argument to parameterize the requirements file
ARG REQUIREMENTS_FILE

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    # For building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev \
    # For troubleshooting
    curl \
    # For installing django-vite from github repo
    git

# Set working directory
ARG APP_HOME=/app
ENV APP_HOME /app
WORKDIR /app

# Python ENV vars
ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install python requirements
COPY ./docker/build/requirements/${REQUIREMENTS_FILE} ./requirements.txt
RUN pip install -r ./requirements.txt

# Copy application code to WORKDIR
COPY ./django_vue_experiments ./django_vue_experiments
COPY ./manage.py ./manage.py
COPY ./docker/images/django/scripts ./docker/images/django/scripts

ENTRYPOINT ./docker/images/django/scripts/entrypoint.sh $0 $@
CMD ./docker/images/django/scripts/start.sh

# ---------------------
# Local
# ---------------------
FROM base as local
ENV \
  DJANGO_ENV="local"

# ---------------------
# Deployed
# ---------------------
FROM base as deployed

ENV \
    DEBUG=false

# ---------------------
# Staging
# ---------------------
FROM deployed as staging

ENV \
  DJANGO_ENV="staging"

# ---------------------
# Production
# ---------------------
FROM deployed as production

ENV \
    DJANGO_ENV="production"
