# pylint: disable=redefined-outer-name
import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def test_password():
    return "TestPass123!"


@pytest.fixture
def create_user(_db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs["password"] = test_password
        if "username" not in kwargs:
            kwargs["username"] = "testuser"
        return django_user_model.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def auto_login_user(_db, client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user
    return make_auto_login


@pytest.fixture
def test_user():
    User = get_user_model()  # pylint: disable=invalid-name
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpass123"
    )
