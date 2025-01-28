from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from okp.fields import OkpImageField, okpImageSizeValidator
from okp.utils import get_abbr, get_slug


class OkpUser(AbstractUser):
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
        blank=True,
        null=True,
    )
    playername = models.CharField(
        verbose_name=_("Playername"),
        max_length=255,
        blank=True,
        null=True,
    )
    abbr = models.CharField(
        verbose_name=_("Abbreviation"),
        max_length=4,
        blank=True,
        null=True,
    )
    is_abbr_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Abbreviation"),
        default=True,
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        blank=True,
        null=True,
    )
    is_slug_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Slug"),
        default=True,
    )
    avatar = OkpImageField(
        verbose_name=_("Avatar"),
        upload_to="users/avatars",
        max_width=200,
        max_height=200,
        blank=True,
        null=True,
        validators=[okpImageSizeValidator],
    )
    cover = OkpImageField(
        verbose_name=_("Cover"),
        upload_to="users/covers",
        max_width=1024,
        max_height=256,
        blank=True,
        null=True,
        validators=[okpImageSizeValidator],
    )
    groups = models.ManyToManyField(
        "okp_users.OkpGroup",
        related_name="user_set",
        related_query_name="user",
        verbose_name=_("Groups"),
        blank=True,
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

    def save(self, *args, **kwargs):
        if self.is_abbr_auto:
            self.abbr = get_abbr(self.name)
        if self.is_slug_auto:
            self.slug = get_slug(self.name, self, OkpUser)
        super().save(*args, **kwargs)


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
