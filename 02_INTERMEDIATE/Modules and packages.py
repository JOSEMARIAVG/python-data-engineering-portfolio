# Once you understand how to import a single file (module), 
# it’s time to work with multiple files organized into packages.

# 1. MODULES RECAP
# --------------------------------------------------------------------------------------------------------
    # Let's say you have a file called "mymath.py" in the same directory:
    #
    # def add(a, b):
    #     return a + b
    #
    # def subtract(a, b):
    #     return a - b
    #
    # You can import and use it like this:

    import mymath

    print("Add:", mymath.add(5, 2))
    print("Subtract:", mymath.subtract(5, 2))

    # You can also import specific functions
    from mymath import add

    print("Add (direct import):", add(10, 3))


# 2. PACKAGES (FOLDERS WITH MULTIPLE MODULES)
# --------------------------------------------------------------------------------------------------------
    # A package is just a folder that contains an "__init__.py" file (can be empty).
    # Example structure:
    #
    # mypackage/
    # ├── __init__.py
    # ├── math_utils.py
    # └── string_utils.py
    #
    # In "math_utils.py":
    # def multiply(a, b):
    #     return a * b
    #
    # In "string_utils.py":
    # def to_uppercase(text):
    #     return text.upper()
    #
    # In "__init__.py", you can control what is exposed:
    # from .math_utils import multiply
    # from .string_utils import to_uppercase
    #
    # Then you can use:
    #
    from mypackage import multiply, to_uppercase
    print(multiply(3, 4))
    print(to_uppercase("hello"))

# 3. RELATIVE IMPORTS
# --------------------------------------------------------------------------------------------------------
    # Inside a package, you can use relative imports to access other modules.
    #
    # Example: inside "string_utils.py"
    # from .math_utils import multiply
    #
    # This imports from another file inside the same package.

# 4. NAMESPACES AND ALIASES
# --------------------------------------------------------------------------------------------------------
    # You can use aliases to simplify names

    import math as m
    print("Square root (with alias):", m.sqrt(16))

    # You can also import everything (not recommended)
    from math import *
    print(sqrt(25))  # Works, but can cause conflicts if other modules have same function names

# 5. THE __name__ VARIABLE
# --------------------------------------------------------------------------------------------------------
    # Every Python file has a built-in variable called __name__.
    # When the file is run directly, __name__ == "__main__".
    # When imported, __name__ == "module_name".

    # Example content in mymodule.py:
    #
    # def greet():
    #     print("Hello from mymodule!")
    #
    # if __name__ == "__main__":
    #     print("Running mymodule directly!")
    #     greet()
    #
    # When imported: only greet() is available.
    # When run directly: both messages are printed.

# 6. THIRD-PARTY PACKAGES (FROM PYPI)
# --------------------------------------------------------------------------------------------------------
    # You can install external packages using pip from your terminal:
    pip install requests
    
    # Example:
    import requests
    response = requests.get("https://api.github.com")
    print(response.status_code)