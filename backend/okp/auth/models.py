from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class OkpGroupManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)

    def visible(self):
        return self.filter(is_visible=True)


class OkpGroup(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120,
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
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        blank=True,
        null=True,
    )
    groups = models.ManyToManyField(
        OkpGroup,
        related_name="users",
        verbose_name=_("Groups"),
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["username"]

    def __str__(self):
        return self.name or self.username

    def save(self, *args, **kwargs):
        self.name = (
            f"{self.first_name} {self.last_name}".strip()
            or self.first_name
            or self.username
        )
        super().save(*args, **kwargs)
