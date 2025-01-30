from django.contrib.auth.models import AbstractUser, Permission
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from okp.core.fields import OkpImageField
from okp.core.utils import get_abbr, get_slug
from okp.core.validators import okpImageSizeValidator


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

    def __str__(self):
        return self.name


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
            okpImageSizeValidator,
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])
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
            okpImageSizeValidator,
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])
        ],
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
        return self.name

    def save(self, *args, **kwargs):
        if self.is_name_auto:
            self.name = " ".join(
                filter(None, [
                    self.first_name,
                    self.middle_name,
                    self.last_name,
                ])
            ) or self.username
        if self.is_abbr_auto:
            self.abbr = get_abbr(self.name)
        if self.is_slug_auto:
            self.slug = get_slug(self.name, self, OkpUser)
        super().save(*args, **kwargs)
