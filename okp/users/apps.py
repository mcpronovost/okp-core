from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OkpUsersConfig(AppConfig):
    name = "okp.users"
    label = "okp_users"
    verbose_name = _("Authentication & Authorization")
