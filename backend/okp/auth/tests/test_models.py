# pylint: disable=invalid-name
import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestOkpUser:
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

    def test_auto_generated_fields(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="johnsmith",
            first_name="John",
            last_name="Smith",
            email="john@example.com",
            password="testpass123"
        )
        assert user.name == "John Smith"  # Auto-generated name
        assert user.abbr == "JS"  # Auto-generated abbreviation
        assert user.slug == "john-smith"  # Auto-generated slug
