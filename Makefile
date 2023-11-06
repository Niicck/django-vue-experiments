SHELL := /bin/bash
-include .env

VERSION := $(shell python -c "from django_vue_experiments import __version__; print(__version__)")

# ---------------------
# Setup
# ---------------------

# Create .env from template if .env doesn't already exist
.env:
	cp -n ./.env-sample .env

# Install pre-commit
.PHONY: install-pre-commit
install-pre-commit:
	pre-commit install

.PHONY: install-tox
install-tox:
	pip install --upgrade tox

.PHONY: setup
setup: .env install-pre-commit install-tox

# ---------------------
# Run on Docker
# ---------------------

DOCKER_COMPOSE_DIR := ./docker/compose

# Run your django app docker container
.PHONY: docker-up
docker-up:
	docker compose \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.yml \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.local.yml \
		--env-file .env \
		up

# Run your production django app docker container
.PHONY: docker-up
docker-up-production:
	docker compose \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.yml \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.production.yml \
		--env-file .env \
		up

# Kill and restart your django app docker container
.PHONY: docker-restart
docker-restart:
	docker compose \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.yml \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.local.yml \
		--env-file .env \
		kill app
	docker compose \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.yml \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.local.yml \
		--env-file .env \
		restart app

# Run a django app docker container without runserver
.PHONY: docker-troubleshoot
docker-troubleshoot:
	docker compose \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.yml \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.local.yml \
		-f ${DOCKER_COMPOSE_DIR}/docker-compose.troubleshooting.yml \
		--env-file .env \
		up

# Enter into the postgres db shell inside your running postgres container
.PHONY: db-shell
db-shell:
	docker exec -it ${COMPOSE_PROJECT_NAME}-db-1 psql -U ${POSTGRES_USER} -p ${POSTGRES_PORT}  -d ${POSTGRES_DB} -w

# Enter into a bash shell inside your running django app docker container
.PHONY: shell
shell:
	docker exec -it ${COMPOSE_PROJECT_NAME}-app-1 /bin/bash

# Enter into the django python shell inside your running django app docker container
.PHONY: docker-shell-plus
shell-plus:
	docker exec -it ${COMPOSE_PROJECT_NAME}-app-1 python manage.py shell_plus

# ---------------------
# Build
# ---------------------

# collect static django assets
.PHONY: collectstatic
collectstatic:
	poetry run python manage.py collectstatic --noinput

# compile vite assets for production
.PHONY: build-vite
build-vite:
	npm run build

# Build "docker/build/requirements/dev.txt"
.PHONY: dev-requirements
dev-requirements:
	python ./docker/scripts/build_requirements.py --dev

# Build "docker/build/requirements/production.txt"
.PHONY: production-requirements
production-requirements:
	python ./docker/scripts/build_requirements.py

# Build local django app docker container
.PHONY: build-local
build-local:
	sh ./docker/scripts/build_image.sh local

# Build local django app docker container
build-production:
	sh ./docker/scripts/build_image.sh production
