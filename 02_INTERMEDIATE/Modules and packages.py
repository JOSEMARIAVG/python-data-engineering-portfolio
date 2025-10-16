
# Modules and packages allow you to organize Python code into reusable pieces.
# - A module is a single .py file containing functions, classes, or variables.
# - A package is a folder containing multiple modules and an __init__.py file.

# 1. Importing Standard Modules
# --------------------------------------------------------------------------------------------------------
    # Python provides many built-in modules that can be imported.

    import math       # Provides mathematical functions
    import random     # Provides random number generation
    import datetime   # Provides date and time utilities

    # Using math module
    print("Square root of 16:", math.sqrt(16))
    print("Pi value:", math.pi)

    # Using random module
    print("Random integer between 1 and 10:", random.randint(1, 10))

    # Using datetime module
    print("Current date and time:", datetime.datetime.now())

# 2. Importing Specific Functions or Classes
# --------------------------------------------------------------------------------------------------------
    # You can import only what you need to keep namespace clean.

    from math import factorial, ceil

    print("Factorial of 5:", factorial(5))
    print("Ceiling of 3.7:", ceil(3.7))

# 3. Creating Your Own Module
# --------------------------------------------------------------------------------------------------------
    # Save a file called mymodule.py in the following path:
    # import os
    # print(os.getcwd())

    # mymodule.py
    # def greet(name):
    #     return f"Hello, {name}!"
    # PI = 3.14159

    # Then you can import it:
    import mymodule
    print(mymodule.greet("Jose"))
    print("PI from mymodule:", mymodule.PI)

# 4. Using from-import for your own module
# --------------------------------------------------------------------------------------------------------
    from mymodule import greet, PI
    print(greet("Ana"))
    print(PI)

# 5. Packages (folder with __init__.py)
# --------------------------------------------------------------------------------------------------------
        # Folder structure:
        # mypackage/
        # ├── __init__.py
        # ├── module1.py
        # └── module2.py

    # Usage:
    # from mypackage import module1
    # from mypackage.module2 import some_function

    # __init__.py can be empty or initialize package-level variables
    # It makes Python treat the folder as a package