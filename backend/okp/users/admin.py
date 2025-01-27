from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.translation import gettext_lazy as _, pgettext_lazy


from okp.admin import admin_site
from .models import OkpUser, OkpGroup


@admin.register(OkpUser, site=admin_site)
class OkpUserAdmin(UserAdmin):
    list_display = ("name", "abbr", "email", "is_active")
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
                ("abbr", "is_abbr_auto"),
                ("slug", "is_slug_auto"),
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
        (_("Important dates"), {"fields": ("created_at", "updated_at", "last_login")}),
    )
    readonly_fields = ("created_at", "updated_at", "last_login")


@admin.register(OkpGroup, site=admin_site)
class OkpGroupAdmin(GroupAdmin):
    pass
