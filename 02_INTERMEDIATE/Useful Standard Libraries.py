# Python comes with many built-in modules that simplify common tasks.
# This section covers some widely used libraries.

# 1. datetime
# --------------------------------------------------------------------------------------------------------
    # Provides classes to work with dates and times

    import datetime

    now = datetime.datetime.now()          # Current date and time
    today = datetime.date.today()          # Current date
    future = today + datetime.timedelta(days=7)  # Date 7 days from today

    print("Now:", now)
    print("Today:", today)
    print("Future (7 days later):", future)

# 2. collections
# --------------------------------------------------------------------------------------------------------
    # Provides specialized container datatypes like Counter, defaultdict, namedtuple

    from collections import Counter, defaultdict, namedtuple

    # Counter counts occurrences of elements
    letters = ["a", "b", "a", "c", "b", "a"]
    count = Counter(letters)
    print("Letter counts:", count)

    # defaultdict provides a default value for missing keys
    dd = defaultdict(int)
    dd["x"] += 1
    print("Defaultdict example:", dd)

    # namedtuple creates lightweight object-like tuples
    Point = namedtuple("Point", ["x", "y"])
    p = Point(2, 3)
    print("Point:", p)

# 3. itertools
# --------------------------------------------------------------------------------------------------------
    # Provides tools for efficient looping and combinations

    import itertools

    # Combinations of 2 elements from a list
    items = [1, 2, 3]
    combs = list(itertools.combinations(items, 2))
    print("Combinations:", combs)

    # Permutations of 2 elements
    perms = list(itertools.permutations(items, 2))
    print("Permutations:", perms)

# 4. math
# --------------------------------------------------------------------------------------------------------
    # Provides mathematical functions and constants

    import math

    print("Square root of 16:", math.sqrt(16))
    print("Pi:", math.pi)
    print("Ceiling of 3.7:", math.ceil(3.7))
    print("Floor of 3.7:", math.floor(3.7))

# 5. random
# --------------------------------------------------------------------------------------------------------
    # Provides functions to generate random numbers and choices

    import random

    print("Random integer 1-10:", random.randint(1, 10))
    print("Random choice from list:", random.choice([1, 2, 3, 4]))
    print("Random shuffle of list:", random.sample([1, 2, 3, 4], k=4))  # shuffled copy

# 6. os
# --------------------------------------------------------------------------------------------------------
    # Interact with the operating system (files, directories, environment variables)

    import os

    print("Current working directory:", os.getcwd())
    print("List of files/folders:", os.listdir("."))
    # Create a folder (if it doesn't exist)
    os.makedirs("test_folder", exist_ok=True)

# 7. sys
# --------------------------------------------------------------------------------------------------------
    # Provides access to system-specific parameters and functions

import sys

print("Python version:", sys.version)
print("Script arguments:", sys.argv)  # List of command-line arguments

# 8. re
# --------------------------------------------------------------------------------------------------------
    # Regular expressions for pattern matching in strings

    import re

    text = "My email is example@test.com"
    pattern = r"\S+@\S+\.\S+"
    match = re.search(pattern, text)
    if match:
        print("Found email:", match.group())

# 9. time
# --------------------------------------------------------------------------------------------------------
    # Functions for measuring and controlling time

    import time

    print("Current time (seconds since epoch):", time.time())
    print("Sleeping for 2 seconds...")
    time.sleep(2)
    print("Awake!")

# 10. functools
# --------------------------------------------------------------------------------------------------------
    # Higher-order functions, caching, and functional programming utilities

    import functools

    # Example: caching with lru_cache
    @functools.lru_cache(maxsize=32)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print("Fibonacci(10):", fibonacci(10))