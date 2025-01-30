from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# API documentation patterns
api_doc_patterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/",SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

urlpatterns = [
    path("v1/", include("okp.api.v1.urls")),
    *api_doc_patterns,
]