# Advanced Functional Programming in Python: map, filter, reduce
# This script demonstrates advanced functional programming techniques in Python including:
# 1. Using `map` for transforming iterables
# 2. Using `filter` for selecting elements
# 3. Using `reduce` for cumulative computations
# 4. Combining map, filter, and reduce in functional pipelines
# Each section includes detailed comments and examples.

# 1. USING MAP TO TRANSFORM DATA
# --------------------------------------------------------------------------------------------------------
    # map applies a function to each item in an iterable and returns a new iterable

    numbers = [1, 2, 3, 4, 5]

    # Example 1: square each number
    squared = list(map(lambda x: x**2, numbers))
    print("Squared numbers:", squared)

    # Example 2: convert numbers to strings
    str_numbers = list(map(str, numbers))
    print("Numbers as strings:", str_numbers)


# 2. USING FILTER TO SELECT ELEMENTS
# --------------------------------------------------------------------------------------------------------
    # filter applies a predicate function and returns only elements that satisfy the condition

    # Example 1: keep only even numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers:", even_numbers)

    # Example 2: filter strings longer than 1 character
    words = ["a", "python", "is", "fun"]
    long_words = list(filter(lambda w: len(w) > 1, words))
    print("Long words:", long_words)


# 3. USING REDUCE FOR CUMULATIVE COMPUTATIONS
# --------------------------------------------------------------------------------------------------------
    # reduce applies a function cumulatively to the items of an iterable to reduce it to a single value
    from functools import reduce

    # Example 1: sum of all numbers
    sum_numbers = reduce(lambda x, y: x + y, numbers)
    print("Sum of numbers:", sum_numbers)

    # Example 2: product of all numbers
    product_numbers = reduce(lambda x, y: x * y, numbers)
    print("Product of numbers:", product_numbers)


# 4. COMBINING MAP, FILTER, AND REDUCE
# --------------------------------------------------------------------------------------------------------
    # Functional programming pipelines can be built by chaining map, filter, reduce

    # Example: sum of squares of even numbers
    sum_squares_even = reduce(
        lambda x, y: x + y,                        # reduce function
        map(lambda x: x**2,                        # square each number
            filter(lambda x: x % 2 == 0, numbers) # keep only even numbers
        )
    )
    print("Sum of squares of even numbers:", sum_squares_even)


# 5. ADVANCED EXAMPLE WITH DICTIONARIES
# --------------------------------------------------------------------------------------------------------
    # Using map and filter with dictionaries
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 72},
        {"name": "Charlie", "score": 90},
        {"name": "David", "score": 60}
    ]

    # Get names of students with score >= 80
    top_students = list(
        map(lambda s: s["name"], filter(lambda s: s["score"] >= 80, students))
    )
    print("Top students:", top_students)