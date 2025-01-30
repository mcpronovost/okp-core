from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class OkpGroupManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class OkpGroup(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150,
        unique=True,
    )
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("Permissions"),
        blank=True,
    )
    is_visible = models.BooleanField(
        verbose_name=_("Is Visible"),
        default=True,
    )

    objects = OkpGroupManager()

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")
        ordering = ["name"]


class OkpUser(AbstractUser):
    groups = models.ManyToManyField(
        OkpGroup,
        related_name="users",
        verbose_name=_("Groups"),
        blank=True,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["username"]
