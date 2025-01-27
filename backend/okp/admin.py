from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.models import LogEntry


class CustomAdminSite(AdminSite):
    # Apps order
    app_order = {
        "users": 1,
        "games": 2,
        "forums": 3,
    }

    # Models order
    model_order = {
        "users": {
            "OkpUser": 1,
            "OkpGroup": 2,
        }
    }

    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request)

        # Sort the apps based on the defined order
        app_list.sort(key=lambda x: self.app_order.get(x["app_label"], 999))

        # Sort the models within each app
        for app in app_list:
            if app["app_label"] in self.model_order:
                app["models"].sort(
                    key=lambda x: self.model_order[app["app_label"]].get(
                        x["object_name"], 999
                    )
                )

        return app_list


class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"
    list_display = [
        "action_time",
        "user",
        "content_type",
        "object_repr",
        "action_flag_display",
    ]
    list_filter = [
        "action_flag",
        ("content_type", admin.RelatedOnlyFieldListFilter),
        "user"
    ]
    search_fields = [
        "object_repr",
        "change_message"
    ]
    readonly_fields = [
        "action_time",
        "user",
        "content_type",
        "object_id",
        "object_repr",
        "action_flag",
        "change_message",
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def action_flag_display(self, obj):
        flags = {
            1: "Addition",
            2: "Change",
            3: "Deletion"
        }
        return flags.get(obj.action_flag, "")
    action_flag_display.short_description = "Action"


admin_site = CustomAdminSite()

admin_site.site_title = "OKP Admin"
admin_site.site_header = "Administration"
admin_site.index_title = "Index"

admin.site = admin_site

admin_site.register(LogEntry, LogEntryAdmin)
