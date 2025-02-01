from django.urls import path

from .views import (
    OkpAuthLoginView,
    OkpAuthLogoutView,
    OkpAuthLogoutAllView,
    OkpAuthRegisterView,
)

urlpatterns = [
    path("login/", OkpAuthLoginView.as_view(), name="okp_auth_login"),
    path("logout/", OkpAuthLogoutView.as_view(), name="okp_auth_logout"),
    path(
        "logoutall/", OkpAuthLogoutAllView.as_view(), name="okp_auth_logoutall"
    ),
    path("register/", OkpAuthRegisterView.as_view(), name="okp_auth_register"),
]
