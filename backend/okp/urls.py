"""
URL configuration.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


urlpatterns = [
    path("admin/", admin.site.urls),
    # schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # app
    path("", TemplateView.as_view(template_name="index.html")),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
