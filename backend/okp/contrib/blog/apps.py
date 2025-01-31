from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OkpBlogConfig(AppConfig):
    name = "okp.contrib.blog"
    label = "okp_blog"
    verbose_name = _("Blog")
