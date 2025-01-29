from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OkpCoreConfig(AppConfig):
    name = "okp.core"
    label = "okp_core"
    verbose_name = _("Core")
