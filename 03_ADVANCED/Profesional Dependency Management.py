# This script explains professional ways to manage Python project dependencies
# using pip, poetry, and pipenv. While these are usually command-line tools,
# we will demonstrate the workflow and Python code snippets where relevant.

# 1. PIP (Python Package Installer)
# --------------------------------------------------------------------------------------------------------
    # pip is the standard package manager for Python. It installs packages from PyPI.

    # Example commands (run in terminal):
    # Install a package
    # pip install requests

    # Install a specific version
    # pip install requests==2.31.0

    # List installed packages
    # pip list

    # Freeze requirements to a file for reproducibility
    # pip freeze > requirements.txt

    # Install packages from requirements.txt
    # pip install -r requirements.txt

    # Using pip inside Python to install packages programmatically (not recommended for production):
    import subprocess
    import sys

    package = "requests"
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    # This installs 'requests' from within Python

# 2. POETRY
# --------------------------------------------------------------------------------------------------------
    # Poetry is a modern dependency manager that handles virtual environments, packaging, and publishing.
    # It uses pyproject.toml to track dependencies.

    # Typical workflow (run in terminal):
    # Create a new project
    # poetry new my_project

    # Add dependencies
    # poetry add requests
    # poetry add --dev black  # add a development dependency

    # Install dependencies
    # poetry install

    # Run scripts inside Poetry-managed environment
    # poetry run python script.py

    # Show dependency tree
    # poetry show --tree

# 3. PIPENV
# --------------------------------------------------------------------------------------------------------
    # Pipenv combines pip and virtualenv. It manages virtual environments automatically
    # and uses Pipfile and Pipfile.lock for reproducible installs.

    # Typical workflow (run in terminal):
    # Install pipenv if not already installed
    # pip install pipenv

    # Create a virtual environment and install dependencies
    # pipenv install requests

    # Install a dev dependency
    # pipenv install --dev black

    # Activate the shell for the project
    # pipenv shell

    # Run a command inside the pipenv environment without activating shell
    # pipenv run python script.py

    # Check dependency graph
    # pipenv graph

    # Lock dependencies for reproducibility
    # pipenv lock

# EXTRA: BEST PRACTICES
# --------------------------------------------------------------------------------------------------------
    # - Always use a virtual environment (venv, poetry, or pipenv) to avoid global package conflicts.
    # - Freeze or lock dependencies for reproducibility across machines.
    # - Use dev dependencies separately to avoid bloating production packages.
    # - Prefer poetry or pipenv for modern projects that require strict version control and environment isolation.
    # - Keep your requirements.txt or Pipfile.lock under version control.

    # Example: using pip inside a virtual environment (Python code)
    import os
    venv_path = os.path.join(os.getcwd(), "venv")
    if not os.path.exists(venv_path):
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    print("Virtual environment created at:", venv_path)