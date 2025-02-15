"""Module to start development servers."""

import os
import subprocess
import sys
from pathlib import Path


def terminate_processes(backend_process, frontend_process):
    """
    Terminate the specified backend and frontend processes.
    """
    if "backend_process" in locals():
        backend_process.terminate()
    if "frontend_process" in locals():
        frontend_process.terminate()


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
        terminate_processes(backend_process, frontend_process)

    except subprocess.SubprocessError as e:
        print(f"Subprocess error: {e}")
        terminate_processes(backend_process, frontend_process)
    except OSError as e:
        print(f"OS error: {e}")
        terminate_processes(backend_process, frontend_process)


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
        terminate_processes(backend_process, None)

    except subprocess.SubprocessError as e:
        print(f"Subprocess error: {e}")
        terminate_processes(backend_process, None)
    except OSError as e:
        print(f"OS error: {e}")
        terminate_processes(backend_process, None)


def run_pytest():
    """
    Run the tests for the backend.
    """
    print("\033[93mRunning pytest...\033[0m")
    subprocess.run("pytest -c backend/pytest.ini", shell=True, check=True)
    subprocess.run(
        "coverage erase --rcfile=backend/.coverage",
        shell=True,
        check=True
    )


def run_tests():
    """
    Run the tests for the backend.
    """
    print("\033[93mRunning pylint...\033[0m")
    subprocess.run(
        "pylint --rcfile=backend/.pylintrc --load-plugins pylint_django "
        "--django-settings-module=okp.settings backend/",
        shell=True,
        check=True,
    )
    print("\033[93mRunning flake8...\033[0m")
    subprocess.run(
        "flake8 --config=backend/.flake8 backend/",
        shell=True,
        check=True
    )
    run_pytest()


def main():
    """
    Main function to start development servers or run backend with arguments.
    """
    base_path = Path(__file__).resolve().parent
    backend_path = os.path.join(base_path)
    frontend_path = os.path.join(base_path, "frontend")

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
