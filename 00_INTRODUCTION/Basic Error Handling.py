# 12. Basic Error Handling
# --------------------------------------------------------------------------------------------------------
# Python uses try-except blocks to handle errors (exceptions) gracefully.
# You can also use else and finally for additional control.
# Raising exceptions manually is also possible with the 'raise' statement.

# 1. Basic try-except
# --------------------------------------------------------------------------------------------------------
    try:
        # Attempt to convert user input to integer
        number = int(input("Enter a number: "))
        print("You entered:", number)
    except ValueError:
        # This block executes if the input cannot be converted to integer
        print("Error: That is not a valid integer.")

# 2. Catching multiple exception types
# --------------------------------------------------------------------------------------------------------
    try:
        # Attempt division with user input
        x = int(input("Enter numerator: "))
        y = int(input("Enter denominator: "))
        result = x / y
        print("Result:", result)
    except ValueError:
        # Handles invalid input (non-integer)
        print("Error: Invalid input. Please enter integers.")
    except ZeroDivisionError:
        # Handles division by zero
        print("Error: Cannot divide by zero.")

# 3. Using else
# --------------------------------------------------------------------------------------------------------
    try:
        value = int(input("Enter a positive number: "))
    except ValueError:
        # Executes if there is an exception
        print("Error: Invalid input.")
    else:
        # Executes only if no exception occurred
        print("Successfully entered:", value)

# 4. Using finally
# --------------------------------------------------------------------------------------------------------
    try:
        # Attempt to open a file
        file = open("example.txt", "r") # Python looks for the file in the current working directory (CWD) and you can also use an absolute path to avoid ambiguity
        content = file.read()
    except FileNotFoundError:
        # Executes if the file does not exist
        print("Error: File does not exist.")
    else:
        # Executes if no exception occurred
        print("File content successfully read")
    finally:
        # Always executes, used for cleanup like closing files
        print("This block always executes, cleaning up if needed.")
        try:
            file.close()
        except:
            # If file was never opened, ignore errors
            pass

# 5. Raising Exceptions
# --------------------------------------------------------------------------------------------------------
    def check_positive(n):
        """
        Raises a ValueError if the number is negative.
        Otherwise, returns the number.
        """
        if n < 0:
            raise ValueError("Number must be positive!")
        return n

    try:
        print(check_positive(5))   # Works fine
        print(check_positive(-3))  # Raises exception
    except ValueError as e:
        # Catch the raised exception and display message
        print("Caught an exception:", e)

# 6. Practical Example: Safe division
# --------------------------------------------------------------------------------------------------------
    def safe_divide(a, b):
        """
        Divides a by b safely.
        Returns the result or None if division by zero occurs.
        """
        try:
            return a / b
        except ZeroDivisionError:
            # Handle division by zero
            print("Cannot divide by zero")
            return None

    print("10 / 2 =", safe_divide(10, 2))
    print("10 / 0 =", safe_divide(10, 0))

# This is a list of the most frequently encountered exceptions in Python
# and the situations in which they occur.

# 1. ValueError
# Raised when a function receives an argument of the correct type but an inappropriate value.
# Example: converting a non-numeric string to int.

# 2. TypeError
# Raised when an operation or function is applied to an object of an inappropriate type.
# Example: adding a string to an integer.

# 3. ZeroDivisionError
# Raised when a number is divided by zero.

# 4. IndexError
# Raised when trying to access an element outside the valid range of a list, tuple, or other sequence.

# 5. KeyError
# Raised when trying to access a dictionary with a key that does not exist.

# 6. FileNotFoundError
# Raised when attempting to open a file that does not exist.

# 7. AttributeError
# Raised when trying to access an attribute or method that does not exist for an object.
# Example: calling append() on a string.

# 8. ImportError / ModuleNotFoundError
# Raised when a module cannot be imported or does not exist.
# ModuleNotFoundError is a subclass of ImportError in Python 3.