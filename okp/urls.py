from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
# from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from front.api.router import api_router

urlpatterns = [
    re_path(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"^admin-django/", admin.site.urls),
    re_path(r"^admin/", include(wagtailadmin_urls)),
    re_path(r"^api-wagtail/", api_router.urls),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + i18n_patterns(
    # re_path(r"^", include(wagtail_urls))
)
