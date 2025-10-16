# Virtual environments allow you to create isolated Python environments
# for different projects, preventing dependency conflicts.
# Dependency management ensures your project has all required packages
# and makes it reproducible for others.

## Theoretical Content ##

# 1. Creating a Virtual Environment
# --------------------------------------------------------------------------------------------------------
    # Using venv (built-in module in Python 3.3+)
    # Open a terminal / command prompt and run:

    # Windows:
    # python -m venv env

    # macOS / Linux:
    # python3 -m venv env

    # This creates a folder named 'env' containing a separate Python environment.

# 2. Activating a Virtual Environment
# --------------------------------------------------------------------------------------------------------
    # Windows:
    # .\env\Scripts\activate

    # macOS / Linux:
    # source env/bin/activate

    # After activation, your terminal will show (env) at the beginning.

# 3. Installing Packages
# --------------------------------------------------------------------------------------------------------
    # Use pip to install packages inside the virtual environment:

    # pip install package_name

    # Example:
    # pip install requests
    # pip install pandas

# 4. Listing Installed Packages
# --------------------------------------------------------------------------------------------------------
    # To see which packages are installed in the environment:
    # pip list

# 5. Freezing Dependencies
# --------------------------------------------------------------------------------------------------------
    # Save installed packages to a requirements.txt file so others can replicate your environment:
    # pip freeze > requirements.txt

# 6. Installing from requirements.txt
# --------------------------------------------------------------------------------------------------------
    # To install all dependencies from a project:
    # pip install -r requirements.txt

# 7. Deactivating the Virtual Environment
# --------------------------------------------------------------------------------------------------------
    # Once finished, you can deactivate it:
    # deactivate

# 8. TIPS
# --------------------------------------------------------------------------------------------------------
    # - Use a virtual environment for each project
    # - Always include a requirements.txt file in your repo
    # - Use version numbers for reproducibility, e.g., requests==2.31.0
    # - Avoid installing packages globally to prevent conflicts