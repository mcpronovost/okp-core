import os
import subprocess
import sys
from pathlib import Path


def start_server(python_exec, npm_exec, backend_path, frontend_path):
    """
    Start the backend and the frontend development servers.
    """
    try:
        print("Starting backend development server...")
        # Start backend development server
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
    """
    Run the backend development server with the given arguments.
    """
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


def run_pytest():
    """
    Run the tests for the backend.
    """
    print("\033[93mRunning pytest...\033[0m")
    subprocess.run("pytest", shell=True)
    subprocess.run("coverage erase", shell=True)


def run_tests():
    """
    Run the tests for the backend.
    """
    print("\033[93mRunning pylint...\033[0m")
    subprocess.run("pylint --load-plugins pylint_django --django-settings-module=okp.settings backend/", shell=True)
    print("\033[93mRunning flake8...\033[0m")
    subprocess.run("flake8 backend/", shell=True)
    run_pytest()


def main():
    """
    Main function to start development servers or run backend with arguments.
    """
    BASE_DIR = Path(__file__).resolve().parent
    backend_path = os.path.join(BASE_DIR)
    frontend_path = os.path.join(BASE_DIR, "frontend")

    # Get the current Python interpreter path
    python_exec = sys.executable
    # Use npm.cmd on Windows, npm otherwise
    npm_exec = "npm.cmd" if sys.platform == "win32" else "npm"

    if len(sys.argv) > 1:
        if sys.argv[1] == "pytest":
            run_pytest()
        elif sys.argv[1] == "tests":
            run_tests()
        else:
            backend_args = sys.argv[1:]
            run_backend(python_exec, backend_path, backend_args)
    else:
        start_server(python_exec, npm_exec, backend_path, frontend_path)


if __name__ == "__main__":
    main()
