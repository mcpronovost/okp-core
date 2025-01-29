import os
import subprocess
import sys
from pathlib import Path

def main():
    BASE_DIR = Path(__file__).resolve().parent
    backend_path = os.path.join(BASE_DIR, "backend")
    frontend_path = os.path.join(BASE_DIR, "frontend")
    
    # Get the current Python interpreter path
    python_path = sys.executable
    # Use npm.cmd on Windows, npm otherwise
    npm_command = "npm.cmd" if sys.platform == "win32" else "npm"

    try:
        print("Starting Django development server...")
        # Start Django development server
        backend_process = subprocess.Popen(
            [python_path, "manage.py", "runserver"],
            cwd=backend_path,
        )

        print("Starting frontend server... ", frontend_path)
        # Start frontend server in a separate process
        frontend_process = subprocess.Popen(
            [npm_command, "run", "dev"],
            cwd=frontend_path,
        )

        # Wait for both processes
        backend_process.wait()
        frontend_process.wait()

    except KeyboardInterrupt:
        print("\nStopping servers...")
        backend_process.terminate()
        frontend_process.terminate()

    except Exception as e:
        print(f"Error: {e}")
        if "django_process" in locals():
            backend_process.terminate()
        if "frontend_process" in locals():
            frontend_process.terminate()

if __name__ == "__main__":
    main() 