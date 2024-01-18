"""
Django settings for django_vue_experiments project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import re
from pathlib import Path

import dj_database_url
import django_stubs_ext
from decouple import Csv, config

# Add type-checking for django
django_stubs_ext.monkeypatch()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

# Deployment configs

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="0.0.0.0,", cast=Csv())

# iframe support

CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", default="", cast=Csv())
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SAMESITE = "None"

EXTRA_CSP_FRAME_ANCESTORS = config(
    "EXTRA_CSP_FRAME_ANCESTORS", default="http://localhost:4321,", cast=Csv()
)

CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", default=",", cast=Csv())


# Application definition

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third Party
    "django_vite",
    "django_extensions",
    "corsheaders",
    # Local
    "django_vue_experiments",
    "django_vue_experiments.experiments",
]

MIDDLEWARE = [
    "django_vue_experiments.middleware.CSPFrameAncestorsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "django_vue_experiments.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_vue_experiments.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if config("DATABASE_URL", default=""):
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,
            conn_health_checks=True,
        ),
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": config("DATABASE_ENGINE", default="django.db.backends.sqlite3"),
            "NAME": config("DATABASE_NAME", default=BASE_DIR / "db.sqlite3"),
            "USER": config("DATABASE_USER", default=""),
            "PASSWORD": config("DATABASE_PASSWORD", default=""),
            "HOST": config("DATABASE_HOST", default=""),
            "PORT": config("DATABASE_PORT", default=""),
            "TEST": {"NAME": config("DATABASE_NAME", default=":memory:")},
        },
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "vite_assets_dist"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# ---------------------
# Django Extensions
# ---------------------
SHELL_PLUS = "ipython"

# ---------------------
# whitenoise
# ---------------------
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_IMMUTABLE_FILE_TEST
# https://github.com/MrBin99/django-vite/issues/30
def immutable_file_test(path, url):
    # Match filename with 8 or 12 hex digits before the extension.
    # Vite generates files with 8 hash digits.
    # Django generates files with 12 hash digits.
    # e.g. app.db8f2edc0c8a.js
    return re.match(r"^.+\.[0-9a-f]{8,12}\..+$", url)


WHITENOISE_IMMUTABLE_FILE_TEST = immutable_file_test

# ---------------------
# django-vite
# ---------------------
DJANGO_VITE = {
    "default": {
        "dev_mode": config("DJANGO_VITE_DEV_MODE", default=False, cast=bool),
        "dev_server_port": config("DJANGO_VITE_DEV_SERVER_PORT", default="5173"),
    },
}

# Set static_url_prefix when dev_mode is False
if not DJANGO_VITE["default"]["dev_mode"]:
    DJANGO_VITE["default"]["static_url_prefix"] = "django_vue_experiments/vite"
