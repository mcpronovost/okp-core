import re
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class OkpAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True,
    )
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def create(self, validated_data):
        raise NotImplementedError("OkpAuthTokenSerializer is read-only")

    def update(self, instance, validated_data):
        raise NotImplementedError("OkpAuthTokenSerializer is read-only")

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )

        if not user:
            msg = _("Unable to log in with provided credentials.")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class OkpAuthRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            UniqueValidator(
                queryset=get_user_model().objects.all(),
                message=_("A user with that username already exists.")
            )
        ]
    )
    email = serializers.EmailField(
        write_only=True,
        required=True,
        validators=[
            UniqueValidator(
                queryset=get_user_model().objects.all(),
                message=_("A user with that email already exists.")
            )
        ]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)
    terms_accepted = serializers.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "password2",
                  "first_name", "last_name", "terms_accepted")

    def validate_username(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                _("Username must be at least 3 characters long.")
            )
        if len(value) > 150:
            raise serializers.ValidationError(
                _("Username must be less than 150 characters long.")
            )
        if not re.match(r"^[a-zA-Z0-9_-]+$", value):
            raise serializers.ValidationError(
                _("Username must contain only letters, numbers, \
                  underscores, and hyphens.")
            )
        return value

    def validate_first_name(self, value):
        if len(value) > 150:
            raise serializers.ValidationError(
                _("First name must be less than 150 characters long.")
            )
        return value

    def validate_last_name(self, value):
        if len(value) > 150:
            raise serializers.ValidationError(
                _("Last name must be less than 150 characters long.")
            )
        return value

    def validate_terms_accepted(self, value):
        if not value:
            raise serializers.ValidationError(
                _("You must accept the terms of service.")
            )
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": _("Password fields didn't match.")}
            )
        return attrs

    def create(self, validated_data):
        # Remove non-model fields before creating user
        validated_data.pop("password2")
        validated_data.pop("terms_accepted")
        first_name = getattr(validated_data, "first_name", "")
        last_name = getattr(validated_data, "last_name", "")

        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=first_name,
            last_name=last_name,
        )
        return user
