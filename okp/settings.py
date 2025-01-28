"""
Django settings for okp project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = os.getenv("DJANGO_DEBUG") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")


# Application definition

INSTALLED_APPS = [
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # tiers
    # ...
    # okp
    "okp.users",
    "okp.admin",
    # cleanup
    "django_cleanup.apps.CleanupConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "okp.urls"

WSGI_APPLICATION = "okp.wsgi.application"

AUTH_USER_MODEL = "okp_users.OkpUser"

AUTH_GROUP_MODEL = "okp_users.OkpGroup"


# TEMPLATES
# https://docs.djangoproject.com/en/5.1/ref/settings/#templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "okp" / "admin" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# STORAGES
# https://docs.djangoproject.com/en/5.1/ref/settings/#storages

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = os.getenv("LANGUAGE_CODE")

LANGUAGES = [
    ("en", "English"),
    ("fr", "Français"),
]

TIME_ZONE = os.getenv("TIME_ZONE")

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Date/Time formats
DATETIME_FORMAT = "j F Y, H:i"
SHORT_DATETIME_FORMAT = "Y-m-d H:i"

DATE_FORMAT = "j F Y"
SHORT_DATE_FORMAT = "Y-m-d"

TIME_FORMAT = "H:i"

FORMAT_MODULE_PATH = ["okp.formats"]

LOCALE_PATHS = [BASE_DIR / "okp" / "locale"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "staticmedias"

WHITENOISE_KEEP_ONLY_HASHED_FILES = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
