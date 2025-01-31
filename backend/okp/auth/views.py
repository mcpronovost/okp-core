from django.contrib.auth import login
from django.utils import timezone
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from knox.models import get_token_model
from knox.views import LoginView as KnoxLoginView

from .serializers import OkpAuthTokenSerializer


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
        # user_logged_in.send(sender=request.user.__class__, request=request, user=request.user)
        data = self.get_post_response_data(request, token, instance)
        print(">> data : ", data)
        return Response(
            {
                "message": "OkpAuthLoginView POST",
            }
        )
