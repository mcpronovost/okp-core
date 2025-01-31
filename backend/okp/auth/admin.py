from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _, pgettext_lazy

from .models import OkpUser, OkpGroup, OkpAuthToken


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


@admin.register(OkpGroup)
class OkpGroupAdmin(GroupAdmin):
    list_display = ("name", "is_visible")
    list_filter = ("is_visible",)
    search_fields = ("name",)


@admin.register(OkpAuthToken)
class OkpAuthTokenAdmin(admin.ModelAdmin):
    list_display = ("user", "token_key", "created", "expiry")
    list_filter = ("expiry",)
    search_fields = ("user__name", "user__username", "user__email")
    readonly_fields = (
        "user",
        "token_key",
        "created",
        "expiry",
        "data_agent",
        "data_platform",
        "data_mobile"
    )

    fieldsets = (
        (None, {
            "fields": (
                "user",
                "token_key",
                "created",
                "expiry",
            )
        }),
        (_("Data"), {
            "fields": (
                "data_agent",
                "data_platform",
                "data_mobile",
            )
        }),
    )

    def data_agent(self, obj):
        return obj.data.get("AGENT", "-")
    data_agent.short_description = _("Browser Agent")

    def data_platform(self, obj):
        return obj.data.get("PLATFORM", "-")
    data_platform.short_description = _("Browser Platform")

    def data_mobile(self, obj):
        return obj.data.get("MOBILE", "-")
    data_mobile.short_description = _("Browser Mobile")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.unregister(Group)
