from django.urls import include, path

urlpatterns = [
    path("auth/", include("okp.api.v1.auth.urls")),
]
