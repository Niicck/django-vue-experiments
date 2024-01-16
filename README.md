# django-vue-experiments

A collection of experiments for using Django with Vue.

You can try them yourself at: [TODO](#TODO)
And you can read about them here: [TODO](#TODO)

## Add New experiments

Within `django_vue_experiments/experiments/views.py`:
1. Create a new View that inherits from `ExperimentView`.
2. Add your new view to `experiment_view_classes`.

## Run locally

1. Create a .env file.
   - `make .env`
2. Prepare poetry requirements for docker image
  - `make dev-requirements`
3. Build docker containers for local development
  - `make build-local`
4. Start docker containers
  - `make docker-up`

## Deployment

1. Prepare poetry requirements for production docker image
  - `make production-requirements`
2. Build the production docker image
  - `make build-production`
  - Test it locally: `make docker-up-production`
3. Push to docker repo:
   - Ex: `docker push niicck/django_vue_experiments-production:latest`
4. Pull from docker repo on your deployment server:
  - `docker pull niicck/django_vue_experiments-production:latest`
  - If running on dokku, rebuild the app:
    - `dokku ps:rebuild django-vue-experiments`
