from django.contrib import admin
from django.contrib.admin.models import LogEntry


@admin.register(LogEntry)
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
