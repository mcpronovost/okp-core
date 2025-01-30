from django.conf import settings
from django.contrib import admin
from django.urls import resolve


class OkpAdminOrderMiddleware:
    # Apps order
    app_order = settings.OKP_ADMIN_ORDER_APPS

    # Models order
    model_order = settings.OKP_ADMIN_ORDER_MODELS

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if we're in the admin interface
        if request.path.startswith("/admin/"):
            try:
                url_resolver = resolve(request.path)
                if url_resolver.app_name == "admin":
                    self._sort_admin_menu()
            except:
                pass

        response = self.get_response(request)
        return response

    def _sort_admin_menu(self):
        # Monkey patch the get_app_list method
        original_get_app_list = admin.site.get_app_list

        def get_app_list(request, app_label=None):
            app_list = original_get_app_list(request)

            # Sort the apps based on the defined order
            app_list.sort(key=lambda x: self.app_order.get(
                x["app_label"], 999))

            # Sort the models within each app
            for app in app_list:
                if app["app_label"] in self.model_order:
                    app["models"].sort(
                        key=lambda x: self.model_order[app["app_label"]].get(
                            x["object_name"], 999
                        )
                    )

            return app_list

        admin.site.get_app_list = get_app_list
