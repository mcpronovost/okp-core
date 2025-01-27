from django.contrib import admin
from django.contrib.admin import AdminSite


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

# Replace the default admin site
admin_site = CustomAdminSite()
admin.site = admin_site
