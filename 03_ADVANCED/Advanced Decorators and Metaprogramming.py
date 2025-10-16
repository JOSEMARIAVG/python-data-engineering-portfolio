# -----------------------------
# Advanced Decorators & Metaprogramming in Python
# -----------------------------

# 1. Simple logging decorator
def log_decorator(func):
    """
    Logs the function call with arguments and its return value.
    """
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} finished and returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 5)


# 2. Decorator with parameters
def repeat(times):
    """
    Repeats the execution of the decorated function `times` times.
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
    print(f"Hello {name}")

greet("Jose")


# 3. Class-based decorator
class Timer:
    """
    Measures the execution time of a function.
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
    return sum(range(n))

compute_sum(1000000)


# 4. Metaprogramming: dynamic class creation
def create_class(name, base, attributes):
    """
    Dynamically creates a class with the given name, base class, and attributes.
    """
    return type(name, (base,), attributes)

# Example: create a Person class dynamically
Person = create_class("Person", object, {"greet": lambda self: print("Hello from dynamic class")})

p = Person()
p.greet()


# 5. Metaprogramming: intercept attribute access
class DynamicAttributes:
    """
    Demonstrates custom behavior when accessing undefined attributes.
    """
    def __getattr__(self, name):
        return f"The attribute '{name}' does not exist, but we handled it!"

obj = DynamicAttributes()
print(obj.anything)  # returns a custom message
print(obj.some_value)  # also handled dynamically
