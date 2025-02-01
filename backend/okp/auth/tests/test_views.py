# pylint: disable=invalid-name,redefined-outer-name
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
class TestOkpAuthViews:
    def test_login_success(self, api_client):
        User = get_user_model()
        User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        response = api_client.post(reverse("okp_auth_login"), {
            "username": "testuser",
            "password": "testpass123"
        })

        assert response.status_code == 200
        assert "token" in response.data
        assert "user" in response.data

    def test_login_wrong_credentials(self, api_client):
        response = api_client.post(reverse("okp_auth_login"), {
            "username": "wronguser",
            "password": "wrongpass"
        })
        assert response.status_code == 400

    def test_login_token_limit(self, api_client):
        """Test token limit per user"""
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        for _ in range(3):
            response = api_client.post(reverse("okp_auth_login"), {
                "username": "testuser",
                "password": "testpass123"
            })
            assert response.status_code == 200

        assert user.auth_token_set.count() == 2

    # pylint: disable=unused-argument
    def test_logout_success(self, api_client, test_user):
        # First login to get token
        response = api_client.post(reverse("okp_auth_login"), {
            "username": "testuser",
            "password": "testpass123"
        })
        token = response.data["token"]

        # Then logout
        api_client.credentials(HTTP_AUTHORIZATION=f"okp {token}")
        response = api_client.post(reverse("okp_auth_logout"))
        assert response.status_code == 204

    # pylint: disable=unused-argument
    def test_logoutall_success(self, api_client, test_user):
        # First login to get token
        response = api_client.post(reverse("okp_auth_login"), {
            "username": "testuser",
            "password": "testpass123"
        })
        token = response.data["token"]

        # Then logout
        api_client.credentials(HTTP_AUTHORIZATION=f"okp {token}")
        response = api_client.post(reverse("okp_auth_logoutall"))
        assert response.status_code == 204

    def test_register_success(self, api_client):
        response = api_client.post(reverse("okp_auth_register"), {
            "username": "newuser",
            "email": "new@example.com",
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "terms_accepted": True
        })

        assert response.status_code == 201
        assert "token" in response.data
        assert "user" in response.data

    def test_register_invalid_data(self, api_client):
        """Test registration with invalid data"""
        response = api_client.post(reverse("okp_auth_register"), {
            "username": "t",  # Too short
            "email": "invalid-email",  # Invalid email
            "password": "short",  # Invalid password
            "password2": "different",  # Mismatched passwords
            "terms_accepted": False  # Terms not accepted
        })

        assert response.status_code == 400
        assert "username" in response.data
        assert "email" in response.data
        assert "password" in response.data
        assert "terms_accepted" in response.data

    # pylint: disable=unused-argument
    def test_register_existing_username(self, api_client, test_user):
        """Test registration with existing username"""
        response = api_client.post(reverse("okp_auth_register"), {
            "username": "testuser",  # Already exists
            "email": "new@example.com",
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "terms_accepted": True
        })

        assert response.status_code == 400
        assert "username" in response.data

    # pylint: disable=unused-argument
    def test_register_existing_email(self, api_client, test_user):
        """Test registration with existing email"""
        response = api_client.post(reverse("okp_auth_register"), {
            "username": "newuser",
            "email": "test@example.com",  # Already exists
            "password": "TestPass123!",
            "password2": "TestPass123!",
            "terms_accepted": True
        })

        assert response.status_code == 400
        assert "email" in response.data
