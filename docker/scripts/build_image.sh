#!/bin/bash
set -e -a

source .env

BUILD_TARGET="$1"

if [ -z "$BUILD_TARGET" ]; then
    echo "Please specify an environment: local, staging, or production."
    exit 1
fi

VERSION=$(python -c "from django_vue_experiments import __version__; print(__version__)")

if [ -z "$VERSION" ]; then
    echo "django_vue_experiments/__init__.py does not specify a __version__."
    exit 1
fi

DOCKER_IMAGE_TAG="v${VERSION}"
DOCKER_IMAGE_TAG_LATEST="latest"

DOCKER_COMPOSE_DIR="./docker/compose"
CURRENT_DIR=`dirname "${BASH_SOURCE[0]}"`
PROJECT_ROOT_DIR="$CURRENT_DIR/../.."

# Navigate to project root directory
pushd "$PROJECT_ROOT_DIR" > /dev/null

case $BUILD_TARGET in
    local)
        make dev-requirements
        docker compose \
            -f ${DOCKER_COMPOSE_DIR}/docker-compose.yml \
            -f ${DOCKER_COMPOSE_DIR}/docker-compose.local.yml \
            --env-file .env \
            build
        ;;
    staging)
        echo "TODO"
        exit 1
        ;;
    production)
        make production-requirements
        make build-vite
        make collectstatic
        docker build \
            -f ./docker/images/django/django.Dockerfile \
            -t $DOCKER_IMAGE_REPO:$DOCKER_IMAGE_TAG \
            --target $BUILD_TARGET \
            --build-arg REQUIREMENTS_FILE=production.txt \
            --progress=plain \
            .

        # Add latest tag
        docker tag $DOCKER_IMAGE_REPO:$DOCKER_IMAGE_TAG $DOCKER_IMAGE_REPO:latest
        ;;
    *)
        echo "Invalid environment specified. Use local, staging, or production."
        exit 1
        ;;
esac
