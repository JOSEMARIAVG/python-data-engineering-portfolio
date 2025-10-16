# Examples of Python functions and parameter handling
# Demonstrates defining functions, parameters, default values,
# *args, **kwargs, return statements, and lambda functions.

# 1. Defining a Basic Function
# --------------------------------------------------------------------------------------------------------
    # Functions allow you to encapsulate code for reuse

    def greet():
        """Prints a simple greeting."""
        print("Hello, welcome to my Python Fundamentals to Advanced!")

    greet()  # Call the function

# 2. Function with Parameters
# --------------------------------------------------------------------------------------------------------
    # Functions can accept inputs to perform operations

    def greet_person(name):
        """Greets a person by name."""
        print(f"Hello, {name}!")

    greet_person("Jose")
    greet_person("Ana")

# 3. Function with Default Parameters
# --------------------------------------------------------------------------------------------------------
# You can set default values for parameters

    def greet_person_with_age(name, age=25):
        """Greets a person and shows age (default 25)."""
        print(f"Hello, {name}! You are {age} years old.")

    greet_person_with_age("Luis")
    greet_person_with_age("Maria", 30)

# 4. Function with *args
# --------------------------------------------------------------------------------------------------------
    # *args allows passing a variable number of positional arguments

    def sum_numbers(*args):
        """Sums any number of numeric arguments."""
        total = 0
        for num in args:
            total += num
        return total

    print("Sum with *args:", sum_numbers(1, 2, 3, 4))  # 10
    print("Sum with *args:", sum_numbers(5, 10))       # 15

# 5. Function with **kwargs
# --------------------------------------------------------------------------------------------------------
    # **kwargs allows passing a variable number of keyword arguments

    def print_info(**kwargs):
        """Prints key-value pairs."""
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print("Information using **kwargs:")
    print_info(name="Jose", age=28, city="Huelva")

# 6. Function with Both *args and **kwargs
# --------------------------------------------------------------------------------------------------------
    # You can combine both to accept any number of positional and keyword arguments

    def combined_example(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)

    combined_example(1, 2, 3, name="Ana", age=22)

# 7. Function with Return Values
# --------------------------------------------------------------------------------------------------------
    # Functions can return results to be used later

    def multiply(a, b):
        """Returns the product of two numbers."""
        return a * b

    print("5 * 4 =", multiply(5, 4))

# 8. Lambda Functions
# --------------------------------------------------------------------------------------------------------
# 8. Lambda Functions
# --------------------------------------------------------------------------------------------------------
    # Lambda functions are anonymous, single-expression functions.
    # They are defined in one line using the keyword 'lambda'.
    # They are useful for short operations that do not require a full function definition.

    # Example 1: square of a number
    square = lambda x: x ** 2
    print("Lambda square of 5:", square(5))  # 25

    # Explanation:
    # - 'lambda x:' defines a function that takes one argument 'x'
    # - 'x ** 2' is the single expression it evaluates and returns
    # - Unlike normal functions, there is no 'def' or 'return' keyword
    # - Ideal for simple operations used temporarily

    # Example 2: sum of two numbers
    add = lambda a, b: a + b
    print("Lambda add 3 + 7:", add(3, 7))  # 10

    # Differences from normal functions:
    # 1. Lambda functions can only have one expression (no multiple statements)
    # 2. They do not need a name (can be anonymous), but we can assign a name as above
    # 3. They return the result automatically, no need for 'return'
    # 4. Typically used as arguments to higher-order functions, e.g., map(), filter(), sort()

    # Practical usage example with map()
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda n: n ** 2, numbers)) # map(): applies a function to each element
    print("Squared numbers using lambda and map():", squared_numbers)

    # Practical usage example with filter()
    even_numbers = list(filter(lambda n: n % 2 == 0, numbers)) # filter(): selects elements that satisfy a condition
    print("Even numbers using lambda and filter():", even_numbers)

    # Practical usage example with sort() and key
    words = ["apple", "banana", "cherry", "date"]
    words_sorted_by_length = sorted(words, key=lambda w: len(w))
    # The sorted() function returns a new sorted list from any iterable (list, tuple, string, etc.)
    # It does NOT modify the original iterable.
    # You can sort in ascending (default) or descending order and use a custom key function.
    print("Words sorted by length using lambda:", words_sorted_by_length)

# 9. Practical Example
# --------------------------------------------------------------------------------------------------------
# Combine functions, *args, **kwargs and return values

def student_report(*names, **grades):
    """
    Prints student names and their grades.
    Calculates average grade.
    """
    print("Students:", names)
    total = sum(grades.values())
    count = len(grades)
    print("Len:", count)
    average = total / count if count > 0 else 0
    print("Grades:", grades)
    print("Average grade:", average)

student_report("Ana", "Luis", "Maria", Ana=85, Luis=90, Maria=78)