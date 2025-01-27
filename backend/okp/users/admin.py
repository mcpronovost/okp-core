from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import gettext_lazy as _

from okp.admin import admin_site
from .models import OkpUser, OkpGroup


@admin.register(OkpUser, site=admin_site)
class OkpUserAdmin(UserAdmin):
    list_display = ("name", "email", "is_active")
    list_filter = ("is_active",)
    search_fields = ("username", "playername", "first_name", "last_name", "email")
    fieldsets = (
        (None, {
            "fields": ("username", "email", "password")
        }),
        (_("Identity"), {
            "fields": (
                "first_name",
                "last_name",
                "playername",
            )
        }),
        (
            _("Authorizations"),
            {
                "fields": (
                    "is_active",
                    # "is_staff",
                    # "is_superuser",
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
        (_("Important dates"), {"fields": ("last_login", "created_at", "updated_at")}),
    )
    readonly_fields = ("last_login", "created_at", "updated_at")


@admin.register(OkpGroup, site=admin_site)
class OkpGroupAdmin(GroupAdmin):
    pass
