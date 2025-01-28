from django.conf import settings
from django.core.management.base import BaseCommand
import subprocess
import os
import sys

class Command(BaseCommand):
    help = "Runs both Django and frontend development servers"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting development servers... "))

        frontend_path = os.path.join(settings.BASE_DIR, "okp", "admin", "frontend")
        
        # Use npm.cmd on Windows, npm otherwise
        npm_command = "npm.cmd" if sys.platform == "win32" else "npm"
        # Get the current Python interpreter path
        python_path = sys.executable

        try:
            # Start frontend server in a separate process
            frontend_process = subprocess.Popen(
                [npm_command, "run", "start"],
                cwd=frontend_path,
            )

            # Start Django development server
            django_process = subprocess.Popen(
                [python_path, "manage.py", "runserver"],
            )

            # Wait for both processes
            frontend_process.wait()
            django_process.wait()

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("\nStopping development servers..."))
            frontend_process.terminate()
            django_process.terminate()

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
            if "frontend_process" in locals():
                frontend_process.terminate()
            if "django_process" in locals():
                django_process.terminate()
