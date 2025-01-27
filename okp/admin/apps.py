from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OkpAdminConfig(AppConfig):
    name = "okp.admin"
    label = "okp_admin"
    verbose_name = _("Admin")
