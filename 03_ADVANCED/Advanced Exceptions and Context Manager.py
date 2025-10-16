# Advanced Python Techniques: Decorators, Metaprogramming, and Context Managers
# This script demonstrates advanced Python concepts including:
# 1. Function decorators (simple, with parameters, class-based)
# 2. Metaprogramming techniques (dynamic class creation, attribute interception)
# 3. Context managers using contextlib

# Each section includes detailed comments to explain the behavior and purpose.


# 1. SIMPLE LOGGING DECORATOR
# --------------------------------------------------------------------------------------------------------
    def log_decorator(func):
        """
        Logs the function call with arguments and its return value.
        Useful for debugging and tracing function execution.
        """
        def wrapper(*args, **kwargs):
            print(f"[LOG] Running {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args,**kwargs)
            print(f"[LOG] {func.__name__} finished and returned {result}")
            return result
        return wrapper

    @log_decorator
    def add(a, b):
        """
        Adds two numbers.
        """
        return a + b

    add(3, 5)

# 2. DECORATOR WITH PARAMETERS
# --------------------------------------------------------------------------------------------------------
    def repeat(times):
        """
        Repeats the execution of the decorated function `times` times.
        Shows how to create a decorator that accepts arguments.
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                for i in range(times):
                    print(f"[DEBUG] Iteration {i+1}")
                    func(*args, **kwargs)
            return wrapper
        return decorator

    @repeat(3)
    def greet(name):
        """
        Greets the given name multiple times.
        """
        print(f"Hello {name}")

    greet("Jose")

# 3. CLASS-BASED DECORATOR
# --------------------------------------------------------------------------------------------------------
    class Timer:
        """
        Class-based decorator to measure the execution time of a function.
        Demonstrates the use of __init__ and __call__ in decorators.
        """
        import time

        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            start = self.time.time()
            result = self.func(*args, **kwargs)
            end = self.time.time()
            print(f"[TIMER] {self.func.__name__} executed in {end - start:.4f} seconds")
            return result

    @Timer
    def compute_sum(n):
        """
        Computes the sum of numbers from 0 to n-1.
        """
        return sum(range(n))

    compute_sum(1000000)


# 4. METAPROGRAMMING: DYNAMIC CLASS CREATION
# --------------------------------------------------------------------------------------------------------
    def create_class(name, base, attributes):
        """
        Dynamically creates a class with the given name, base class, and attributes.
        Demonstrates runtime class generation using `type`.
        """
        return type(name, (base,), attributes)

    # Example: create a Person class dynamically
    Person = create_class("Person", object, {"greet": lambda self: print("Hello from dynamic class")})

    p = Person()
    p.greet()


# 5. METAPROGRAMMING: INTERCEPT ATTRIBUTE ACCESS
# --------------------------------------------------------------------------------------------------------
    class DynamicAttributes:
        """
        Demonstrates custom behavior when accessing undefined attributes.
        __getattr__ is called only when the attribute does not exist.
        """
        def __getattr__(self, name):
            return f"The attribute '{name}' does not exist, but we handled it!"

    obj = DynamicAttributes()
    print(obj.anything)    # returns a custom message
    print(obj.some_value)  # also handled dynamically


# 6. CONTEXT MANAGERS (USING contextlib)
# --------------------------------------------------------------------------------------------------------
    from contextlib import contextmanager
    import time

    @contextmanager
    def timer_context(name):
        """
        Context manager to measure execution time of a code block.
        Demonstrates the use of contextlib.contextmanager decorator.
        """
        start = time.time()
        print(f"[CONTEXT] Starting '{name}'...")
        try:
            yield
        finally:
            end = time.time()
            print(f"[CONTEXT] '{name}' finished in {end - start:.4f} seconds")

    # Example usage of context manager
    with timer_context("Sum computation"):
        total = sum(range(1000000))