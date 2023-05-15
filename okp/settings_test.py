from .settings import *
import os

# DB SQLLite in Memory for test only

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

EMAIL_BACKEND = "django.core.mail.backends.localmem.EmailBackend"

DEBUG = False

DEFAULT_PROTOCOL = PROJECT_PROTOCOL = "http://"
DEFAULT_DOMAIN = PROJECT_DOMAIN = os.getenv("LOCAL_IP", "192.168.0.167") + ":8095"
PROJECT_URI = "".join((PROJECT_PROTOCOL, PROJECT_DOMAIN))
EMAIL_BACKEND = "django.core.mail.backends.localmem.EmailBackend"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 5
}
