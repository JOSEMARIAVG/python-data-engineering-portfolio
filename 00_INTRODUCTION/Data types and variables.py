# Examples of basic Python data types and variables
# This script demonstrates integers, floats, strings, booleans,
# variable assignment, multiple assignment and basic operations.

# 1. Integer (int)
# --------------------------------------------------------------------------------------------------------
    # Integers are whole numbers without a decimal part
    age = 25            # Assign an integer value to a variable
    year = 2025         # Another integer

    # Print values and types
    print("Integer examples:")
    print("Age:", age)                  # 25
    print("Year:", year)                # 2025
    print("Type of age:", type(age))    # <class 'int'> shows the variable type
    print("-" * 20)                     # Separator line for clarity

# 2. Floating-point number (float)
# --------------------------------------------------------------------------------------------------------
    # Floats are numbers with a decimal point
    height = 1.75       # height in meters
    temperature = 36.6  # body temperature

    print("Float examples:")
    print("Height:", height)
    print("Temperature:", temperature)
    print("Type of height:", type(height))  # <class 'float'>

# 3. String (str)
# --------------------------------------------------------------------------------------------------------
    # Strings are sequences of characters, enclosed in quotes
    name = "Jose Vazquez"
    greeting = 'Hello world!'

    print("String examples:")
    print("Name:", name)
    print("Greeting:", greeting)
    print("Type of name:", type(name))  # <class 'str'>

    # String operations:
    # Concatenation: combine strings using +
    full_greeting = greeting + " My name is " + name
    print("Concatenated string:", full_greeting)

    # Repetition: repeat strings using *
    print("Repeated string:", "Hi! " * 3)

    # Indexing: access specific characters using []
    print("First character of name:", name[0])  # 'J'
    print("Last character of name:", name[-1])  # 'z'
    

# 4. Boolean (bool)
# --------------------------------------------------------------------------------------------------------
    # Booleans represent True or False values
    is_student = True
    has_job = False

    print("Boolean examples:")
    print("Is student?", is_student)
    print("Has job?", has_job)
    print("Type of is_student:", type(is_student))  # <class 'bool'>

    # Boolean logic operations:
    print("Logical AND (is_student and has_job):", is_student and has_job)  # False
    print("Logical OR (is_student or has_job):", is_student or has_job)     # True
    print("Logical NOT (not is_student):", not is_student)                  # False

# 5. Variable assignment and naming
# --------------------------------------------------------------------------------------------------------
    # Variables store data for later use and can be reassigned
    counter = 10
    print("Counter:", counter)

    counter = counter + 5   # Reassign the variable to a new value
    print("Updated counter:", counter)

    # Rules for variable names:
        # - Must start with a letter or underscore
        # - Can contain letters, numbers, and underscores
        # - Case sensitive
    _my_var = 100
    myVar = 200
    print("_my_var:", _my_var)
    print("myVar:", myVar)

# 6. Multiple assignments
# --------------------------------------------------------------------------------------------------------
    # Assign multiple variables in one line
    x, y, z = 1, 2.5, "Python"
    print("x:", x, "| y:", y, "| z:", z)

    # Swapping values without using a temporary variable
    x, y = y, x
    print("After swap -> x:", x, "| y:", y)