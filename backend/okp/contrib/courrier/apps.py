from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class OkpCourrierConfig(AppConfig):
    name = "okp.contrib.courrier"
    label = "okp_courrier"
    verbose_name = _("Courrier")
