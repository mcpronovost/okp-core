from django.core.management.base import BaseCommand
from django.utils import timezone

from okp.auth.models import OkpAuthToken


class Command(BaseCommand):
    # command: python manage.py clean_expired_tokens
    help = "Removes expired OkpAuthTokens from the database"

    def handle(self, *args, **options):
        self.stdout.write("\nCleaning expired OkpAuthTokens...\n")
        now = timezone.now()
        deleted_count, _ = OkpAuthToken.objects.filter(expiry__lt=now).delete()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully deleted {deleted_count} expired tokens"
            )
        )
        self.stdout.write("Done.\n\n")
