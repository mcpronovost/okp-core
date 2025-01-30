from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from .models import OkpUser


@admin.register(OkpUser)
class OkpUserAdmin(UserAdmin):
    list_display = ("name", "email", "is_active")
    list_filter = ("is_active",)
    filter_horizontal = ("groups", "user_permissions")
    search_fields = ("username", "name", "email")
    readonly_fields = ("created_at", "updated_at", "last_login")

    fieldsets = (
        (None, {
            "fields": ("username", "email", "password")
        }),
        (_("Identity"), {
            "fields": (
                "first_name",
                "middle_name",
                "last_name",
                ("name", "is_name_auto"),
                ("abbr", "is_abbr_auto"),
                ("slug", "is_slug_auto"),
            )
        }),
        (_("Media"), {
            "fields": (
                "avatar",
                "cover",
            )
        }),
        (
            pgettext_lazy("admin_is_boolean", "Status"),
            {
                "fields": (
                    "is_active",
                ),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (_("Important dates"), {
            "fields": (
                "created_at",
                "updated_at",
                "last_login",
            )
        }),
    )
