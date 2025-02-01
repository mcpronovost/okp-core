import pytest
from django.contrib.auth import get_user_model

from okp.auth.serializers import (
    OkpAuthRegisterSerializer,
    OkpAuthTokenSerializer
)


@pytest.mark.django_db
class TestOkpAuthTokenSerializer:
    def test_token_serializer_valid_credentials(self):
        User = get_user_model()  # pylint: disable=invalid-name
        User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        data = {
            "username": "testuser",
            "password": "testpass123"
        }
        serializer = OkpAuthTokenSerializer(data=data)
        assert serializer.is_valid()

    def test_create_not_implemented(self):
        """Test create method raises NotImplementedError"""
        serializer = OkpAuthTokenSerializer()
        with pytest.raises(NotImplementedError) as exc:
            serializer.create({})
        assert str(exc.value) == "OkpAuthTokenSerializer is read-only"

    def test_update_not_implemented(self):
        """Test update method raises NotImplementedError"""
        serializer = OkpAuthTokenSerializer()
        with pytest.raises(NotImplementedError) as exc:
            serializer.update(None, {})
        assert str(exc.value) == "OkpAuthTokenSerializer is read-only"


@pytest.mark.django_db
class TestOkpAuthRegisterSerializer:
    def test_register_serializer_valid_data(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "first_name": "Test",
            "last_name": "User",
            "terms_accepted": True
        }
        serializer = OkpAuthRegisterSerializer(data=data)
        assert serializer.is_valid()

    def test_register_serializer_username_too_short(self):
        data = {
            "username": "t",
            "email": "test@example.com",
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "terms_accepted": True
        }
        serializer = OkpAuthRegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "username" in serializer.errors

    def test_register_serializer_username_too_long(self):
        data = {
            "username": "t" * 151,
            "email": "test@example.com",
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "terms_accepted": True

        }
        serializer = OkpAuthRegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "username" in serializer.errors

    def test_register_serializer_username_invalid_character(self):
        data = {
            "username": "test@user",
            "email": "test@example.com",
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "terms_accepted": True
        }
        serializer = OkpAuthRegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "username" in serializer.errors

    def test_register_serializer_passwords_mismatch(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "TestPass123!",
            "password2": "DifferentPass123!",
            "terms_accepted": True
        }
        serializer = OkpAuthRegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "password" in serializer.errors

    def test_register_serializer_names_too_long(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "first_name": "T" * 151,
            "last_name": "T" * 151,
            "terms_accepted": True
        }
        serializer = OkpAuthRegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert "first_name" in serializer.errors
        assert "last_name" in serializer.errors
