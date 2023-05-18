from .settings import *
import os

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": "db",
        "PORT": "5432",
    }
}

WAGTAILADMIN_BASE_URL = "http://localhost:8000"

DEFAULT_PROTOCOL = PROJECT_PROTOCOL = "http://"
DEFAULT_DOMAIN = PROJECT_DOMAIN = "localhost:8000"
PROJECT_URI = "".join((PROJECT_PROTOCOL, PROJECT_DOMAIN))
