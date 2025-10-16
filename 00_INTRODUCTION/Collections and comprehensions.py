# Examples of Python collections and comprehensions
# Demonstrates list, tuple, set, dictionary, and different types of comprehensions.

# 1. Lists
# --------------------------------------------------------------------------------------------------------
    # Ordered, mutable (can be changed), and allow duplicates

    fruits = ["apple", "banana", "cherry"]
    print("Lists:")
    print("Original list:", fruits)

    # Access elements
    print("First element:", fruits[0])

    # Modify an element
    fruits[1] = "blueberry"
    print("Modified list:", fruits)

    # Add elements
    fruits.append("orange")
    print("After append:", fruits)

    # Remove elements
    fruits.remove("apple")
    print("After remove:", fruits)

    # Iterate through list
    for fruit in fruits:
        print("Fruit:", fruit)

# 2. Tuples
# --------------------------------------------------------------------------------------------------------
    # Ordered, immutable (cannot be changed), and allow duplicates

    colors = ("red", "green", "blue")
    print("Tuples:")
    print("Tuple:", colors)
    print("First color:", colors[0])

    # Tuples cannot be modified, but you can create new ones
    new_colors = colors + ("yellow",)
    print("New tuple:", new_colors)

# 3. Sets
# --------------------------------------------------------------------------------------------------------
    # Unordered, mutable, and do not allow duplicates

    numbers = {1, 2, 3, 3, 4}
    print("Original set (duplicates removed):", numbers)

    # Add an element
    numbers.add(5)
    print("After add:", numbers)

    # Remove an element
    numbers.discard(2)
    print("After discard:", numbers)

    # Set operations
    even = {2, 4, 6}
    odd = {1, 3, 5}
    print("Union:", even | odd)
    print("Intersection:", even & odd)
    print("Difference:", even - odd)
    print("Symmetric difference:", even ^ odd)

# 4. Dictionaries
# --------------------------------------------------------------------------------------------------------
    # Key-value pairs, mutable, and unordered

    person = {"name": "Jose", "age": 28, "city": "Huelva"}
    print("Original dictionary:", person)

    # Access a value
    print("Name:", person["name"])

    # Add or modify a key-value pair
    person["country"] = "Spain"
    print("After adding 'country':", person)

    # Remove a key-value pair
    del person["city"]
    print("After removing 'city':", person)

    # Iterate through keys and values
    for key, value in person.items():
        print(f"{key}: {value}")

# 5. List Comprehensions
# --------------------------------------------------------------------------------------------------------
    # Provide a concise way to create lists

    numbers = [1, 2, 3, 4, 5]
    squares = [n ** 2 for n in numbers]

    print("Original numbers:", numbers)
    print("Squares:", squares)

    # Conditional comprehension
    even_squares = [n ** 2 for n in numbers if n % 2 == 0]
    print("Even squares:", even_squares)

# 6. Dictionary Comprehensions
# --------------------------------------------------------------------------------------------------------
    # Create dictionaries in one line

    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]

    people = {name: age for name, age in zip(names, ages)}
    print("People dict:", people)

    # Conditional comprehension
    adults = {name: age for name, age in people.items() if age >= 30}
    print("Adults:", adults)

# 7. Set Comprehensions
# --------------------------------------------------------------------------------------------------------
    # Similar to list comprehensions but for sets (unique values)

    nums = [1, 2, 2, 3, 4, 4, 5]
    unique_squares = {n ** 2 for n in nums}
    print("Unique squares:", unique_squares)

# 8. Tuple Comprehensions (using generator expression)
# --------------------------------------------------------------------------------------------------------
    # Tuples themselves don’t support comprehension syntax directly,
    # but you can use a generator expression and convert it to a tuple.

    gen_tuple = tuple(n * 2 for n in range(5))
    print("Tuple (via generator expression):", gen_tuple)

# 9. Practical Example
# --------------------------------------------------------------------------------------------------------
    # Combining different collection types and comprehensions

    students = [
        {"name": "Ana", "grade": 85},
        {"name": "Luis", "grade": 42},
        {"name": "María", "grade": 73},
    ]

    # Extract passed students using list comprehension
    passed_students = [s["name"] for s in students if s["grade"] >= 60]
    print("Students who passed:", passed_students)

    # Create a dictionary with student names and pass/fail
    results = {s["name"]: ("Pass" if s["grade"] >= 60 else "Fail") for s in students}
    print("Results dict:", results)
