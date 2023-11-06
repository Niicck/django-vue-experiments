FROM node:19-bullseye-slim

# Set working directory
ARG APP_HOME=/app
WORKDIR /app

# Install node modules
COPY ./package.json /app
COPY ./package-lock.json /app
RUN npm install && npm cache clean --force

# Copy application code to WORKDIR
COPY ./vite.config.js .
COPY ./tailwind.config.js .
COPY ./tsconfig.json .
COPY ./django_vue_experiments .
COPY ./docker/images/vite/scripts ./docker/images/vite/scripts

ENTRYPOINT ./docker/images/vite/scripts/entrypoint.sh
