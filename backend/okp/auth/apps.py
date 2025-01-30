from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OkpAuthConfig(AppConfig):
    name = "okp.auth"
    label = "okp_auth"
    verbose_name = _("Authentication")
