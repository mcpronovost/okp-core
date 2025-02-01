from django.contrib.auth import login
from django.contrib.auth.signals import user_logged_in
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from knox.models import get_token_model
from knox.views import (
    LoginView as KnoxLoginView,
    LogoutView as KnoxLogoutView,
    LogoutAllView as KnoxLogoutAllView
)

from .serializers import OkpAuthTokenSerializer, OkpAuthRegisterSerializer


class OkpAuthLoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def get_auth_data(self):
        return {
            "AGENT": self.request.META.get("HTTP_SEC_CH_UA", "-"),
            "PLATFORM": self.request.META.get("HTTP_SEC_CH_UA_PLATFORM", "-"),
            "MOBILE": self.request.META.get("HTTP_SEC_CH_UA_MOBILE", "-"),
        }

    def create_token(self):
        return get_token_model().objects.create(
            user=self.request.user,
            expiry=self.get_token_ttl(),
            prefix=self.get_token_prefix(),
            data=self.get_auth_data(),
        )

    def post(self, request, *args, **kwargs):
        serializer = OkpAuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if (
            token_limit_per_user := self.get_token_limit_per_user()
        ) is not None:
            now = timezone.now()
            tokens = user.auth_token_set.filter(expiry__gt=now)
            if tokens.count() >= token_limit_per_user:
                tokens.first().delete()
        login(request, user)
        instance, token = self.create_token()
        user_logged_in.send(
            sender=request.user.__class__, request=request, user=request.user
        )
        data = self.get_post_response_data(request, token, instance)

        return Response({
            "token": data["token"],
            "user": data["user"],
        })


class OkpAuthLogoutView(KnoxLogoutView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OkpAuthLogoutAllView(KnoxLogoutAllView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class OkpAuthRegisterView(OkpAuthLoginView):
    """
    Register a new user and log them in automatically
    """
    def post(self, request, *args, **kwargs):
        serializer = OkpAuthRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        # Create new user
        user = serializer.save()

        # Log the user in
        login(request, user)
        instance, token = self.create_token()
        user_logged_in.send(
            sender=user.__class__, request=request, user=user
        )
        data = self.get_post_response_data(request, token, instance)

        return Response({
            "token": data["token"],
            "user": data["user"],
        }, status=HTTP_201_CREATED)
