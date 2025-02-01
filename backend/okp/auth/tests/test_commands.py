import pytest
from django.core.management import call_command
from datetime import timedelta
from io import StringIO

from okp.auth.models import OkpAuthToken


@pytest.mark.django_db
class TestCleanExpiredTokens:
    def test_clean_expired_tokens(self, test_user):
        """Test cleaning expired tokens"""
        # Create expired token
        expired_token, _ = OkpAuthToken.objects.create(
            user=test_user,
            expiry=-timedelta(days=1)
        )

        # Create valid token
        valid_token, _ = OkpAuthToken.objects.create(
            user=test_user,
            expiry=timedelta(days=1)
        )

        # Call command
        out = StringIO()
        call_command("clean_expired_tokens", stdout=out)
        output = out.getvalue()

        # Check that only expired token was deleted
        assert "Successfully deleted 1 expired tokens" in output
        assert not OkpAuthToken.objects.filter(pk=expired_token.pk).exists()
        assert OkpAuthToken.objects.filter(pk=valid_token.pk).exists()

    def test_clean_no_expired_tokens(self, test_user):
        """Test cleaning when no expired tokens exist"""
        # Create only valid token
        OkpAuthToken.objects.create(
            user=test_user,
            expiry=timedelta(days=1)
        )

        # Call command
        out = StringIO()
        call_command("clean_expired_tokens", stdout=out)
        output = out.getvalue()

        # Check output
        assert "Successfully deleted 0 expired tokens" in output
