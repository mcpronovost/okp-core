from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

class OkpUser(AbstractUser):
    playername = models.CharField(
        verbose_name=_("Playername"),
        max_length=255,
        blank=True,
        null=True,
    )
    groups = models.ManyToManyField(
        "users.OkpGroup",
        verbose_name=_("Groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-id"]

    def __str__(self):
        return self.name

    @property
    def name(self):
        return (
            self.playername
            or f"{self.first_name} {self.last_name}".strip()
            or self.first_name
            or self.username
        )

class OkpGroup(Group):
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")
        ordering = ["name", "-id"]

    def __str__(self):
        return self.name
