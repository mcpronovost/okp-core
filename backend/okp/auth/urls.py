from django.urls import path
from knox import views as knox_views

from .views import OkpAuthLoginView

urlpatterns = [
    path("login/", OkpAuthLoginView.as_view(), name="okp_auth_login"),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(
        "logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"
    ),
]
