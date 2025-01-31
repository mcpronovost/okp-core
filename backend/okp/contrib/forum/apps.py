from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OkpForumConfig(AppConfig):
    name = "okp.contrib.forum"
    label = "okp_forum"
    verbose_name = _("Forum")
