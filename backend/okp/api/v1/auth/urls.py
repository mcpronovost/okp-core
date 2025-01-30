from django.urls import path
from .views import (
    MeView,
    # LoginView,
    # LogoutView,
    # LogoutAllView,
)

urlpatterns = [
    path("me/", MeView.as_view(), name="me"),
    # path("login/", LoginView.as_view(), name="knox_login"),
    # path("logout/", LogoutView.as_view(), name="knox_logout"),
    # path("logoutall/", LogoutAllView.as_view(), name="knox_logoutall"),
]
