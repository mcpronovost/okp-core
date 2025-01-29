import os
import subprocess
import sys
from pathlib import Path


def start_server(python_exec, npm_exec, backend_path, frontend_path):
    try:
        print("Starting Django development server...")
        # Start Django development server
        backend_process = subprocess.Popen(
            [python_exec, "backend/manage.py", "runserver"],
            cwd=backend_path,
        )

        print("Starting frontend server... ")
        # Start frontend server in a separate process
        frontend_process = subprocess.Popen(
            [npm_exec, "run", "dev"],
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
        if "backend_process" in locals():
            backend_process.terminate()
        if "frontend_process" in locals():
            frontend_process.terminate()

def run_backend(python_exec, backend_path, backend_args):
    try:
        backend_process = subprocess.Popen(
            [python_exec, "backend/manage.py", *backend_args],
            cwd=backend_path,
        )
        backend_process.wait()

    except KeyboardInterrupt:
        print("\nStopping server...")
        backend_process.terminate()

    except Exception as e:
        print(f"Error: {e}")
        if "backend_process" in locals():
            backend_process.terminate()


def main():
    BASE_DIR = Path(__file__).resolve().parent
    backend_path = os.path.join(BASE_DIR)
    frontend_path = os.path.join(BASE_DIR, "frontend")

    # Get the current Python interpreter path
    python_exec = sys.executable
    # Use npm.cmd on Windows, npm otherwise
    npm_exec = "npm.cmd" if sys.platform == "win32" else "npm"

    if len(sys.argv) > 1:
        backend_args = sys.argv[1:]
        run_backend(python_exec, backend_path, backend_args)
    else:
        start_server(python_exec, npm_exec, backend_path, frontend_path)

if __name__ == "__main__":
    main() 