# This section covers advanced Python function features:
# - Decorators: functions that modify other functions
# - Closures: functions that capture variables from their enclosing scope

# 1. Decorators
# --------------------------------------------------------------------------------------------------------
    # A decorator is a function that takes another function and extends or modifies its behavior.

    # Basic decorator example
    def my_decorator(func):
        def wrapper():
            print("Before calling the function")
            func()
            print("After calling the function")
        return wrapper

    @my_decorator  # This is equivalent to my_decorator(say_hello())
    def say_hello():
        print("Hello!")

    say_hello()

    # Decorator with arguments
    def my_decorator_repeat(n):
        """Repeats a function n times"""
        def decorator(func):
            def wrapper(*args):
                for _ in range(n):
                    func(*args)
            return wrapper
        return decorator

    @my_decorator_repeat(3)
    def greet(name):
        print(f"Hi {name}!")

    greet("Jose")

# 2. Closures
# --------------------------------------------------------------------------------------------------------
    # A closure is a function that remembers values from its enclosing scope even after that scope has finished.

    def make_multiplier(factor):
        """Creates a function that multiplies by a given factor"""
        def multiplier(number):
            return number * factor
        return multiplier  # Returns the inner function


    double = make_multiplier(2)
    triple = make_multiplier(3)

    print("Double 5:", double(5))  # 10
    print("Triple 5:", triple(5))  # 15


    # Closures are useful for:
    # - Creating customized functions dynamically
    # - Encapsulating data without using classes