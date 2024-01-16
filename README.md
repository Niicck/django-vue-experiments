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
2. Build docker containers for local development
  - `make build-local`
3. Start docker containers
  - `make docker-up`

## Build for production

1. Update the `__version__` in `django_vue_experiments/__init__.py`.
2. Build the production docker image
  - `make build-production`
  - Test it locally: `make docker-up-production`
3. Push to docker repo:
   - Ex: `docker push niicck/django_vue_experiments:latest`
