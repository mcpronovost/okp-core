"""
URL configuration for okp project.
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from okp.admin import admin_site

urlpatterns = [
    path("admin/", admin_site.urls),
]

urlpatterns += i18n_patterns(
    # path("", include("pages.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
