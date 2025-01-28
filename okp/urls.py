"""
URL configuration for okp project.
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

# from okp.admin import admin_site

urlpatterns = [
    # path("admin/", admin_site.urls),
]

urlpatterns += i18n_patterns(
    # path("admin/", admin_site.urls),
    path(
        "admin/<path:path>",
        TemplateView.as_view(template_name="okp-admin/index.html"),
        name="okp_admin_path"
    ),
    path(
        "admin/",
        TemplateView.as_view(template_name="okp-admin/index.html"),
        name="okp_admin"
    ),
    # path("", include("pages.urls")),
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
