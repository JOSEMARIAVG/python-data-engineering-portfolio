# Advanced Iterators and Generators in Python
# This script demonstrates advanced techniques with iterators and generators including:
# 1. Creating custom iterators
# 2. Using generators with `yield`
# 3. Using `next` to manually iterate
# 4. Generator expressions
# 5. Infinite generators
# Each section includes detailed comments and examples.

# 1. CREATING A CUSTOM ITERATOR
# --------------------------------------------------------------------------------------------------------
    # Custom iterators are objects that implement __iter__() and __next__()

    class Countdown:
        """
        Iterator that counts down from a given number to zero.
        """
        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self  # iterator object must return itself

        def __next__(self):
            if self.current <= 0:
                raise StopIteration  # stop iteration when done
            else:
                value = self.current
                self.current -= 1
                return value

    # Example usage
    for number in Countdown(5):
        print("Countdown:", number)


# 2. GENERATORS USING YIELD
# --------------------------------------------------------------------------------------------------------
    # Generators are simpler iterators using `yield` instead of __next__ and __iter__

    def countdown_gen(start):
        """
        Generator that counts down from start to 1.
        """
        while start > 0:
            yield start  # pause here and return value
            start -= 1

    # Example usage
    for number in countdown_gen(5):
        print("Generator countdown:", number)


# 3. USING NEXT TO MANUALLY ITERATE
# --------------------------------------------------------------------------------------------------------
    # You can use `next()` to manually get values from an iterator or generator

    gen = countdown_gen(3)
    print(next(gen))  # returns 3
    print(next(gen))  # returns 2
    print(next(gen))  # returns 1
    print(next(gen)) #  next(gen)  # would raise StopIteration


# 4. GENERATOR EXPRESSIONS
# --------------------------------------------------------------------------------------------------------
    # Generator expressions are similar to list comprehensions but lazy (do not store all items in memory)

    numbers = range(10)
    squared_gen = (x**2 for x in numbers if x % 2 == 0)  # squares of even numbers

    for value in squared_gen:
        print("Squared even number:", value)


# 5. INFINITE GENERATORS
# --------------------------------------------------------------------------------------------------------
    # Generators can produce infinite sequences without consuming memory

    def infinite_sequence(start=0):
        """
        Infinite generator of numbers starting from `start`.
        """
        num = start
        while True:
            yield num
            num += 1

    # Example usage (take first 5 numbers)
    gen = infinite_sequence(10)
    for _ in range(5):
        print("Infinite sequence number:", next(gen))