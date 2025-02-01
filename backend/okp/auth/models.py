from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from knox.models import AbstractAuthToken

from okp.core.fields import OkpImageField
from okp.core.utils import get_abbr, get_slug
from okp.core.validators import okp_image_size_validator


class OkpUser(AbstractUser):
    email = models.EmailField(
        verbose_name=_("email address"),
        blank=True,
    )
    middle_name = models.CharField(
        verbose_name=_("Middle Name"),
        max_length=150,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_("Public Name"),
        max_length=500,
        blank=True,
        null=True,
    )
    is_name_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Name"),
        default=True,
    )
    abbr = models.CharField(
        verbose_name=_("Abbreviation"),
        max_length=4,
        blank=True,
    )
    is_abbr_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Abbreviation"),
        default=True,
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        blank=True,
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
        validators=[
            okp_image_size_validator,
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "webp"]
            ),
        ],
    )
    cover = OkpImageField(
        verbose_name=_("Cover"),
        upload_to="users/covers",
        max_width=1024,
        max_height=256,
        blank=True,
        null=True,
        validators=[
            okp_image_size_validator,
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "webp"]
            ),
        ],
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
        return self.name

    def save(self, *args, **kwargs):
        if self.is_name_auto:
            self.name = (
                " ".join(
                    name
                    for name in (
                        self.first_name,
                        self.middle_name,
                        self.last_name,
                    )
                    if name
                )
                or self.username
            )
        if self.is_abbr_auto:
            self.abbr = get_abbr(self.name)
        if self.is_slug_auto:
            self.slug = get_slug(self.name, self, OkpUser)
        super().save(*args, **kwargs)


class OkpAuthToken(AbstractAuthToken):
    data = models.JSONField(
        verbose_name=_("Data"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Auth Token")
        verbose_name_plural = _("Auth Tokens")
        ordering = ["user", "expiry"]

    def __str__(self):
        return f"{self.user} - {self.token_key}"
