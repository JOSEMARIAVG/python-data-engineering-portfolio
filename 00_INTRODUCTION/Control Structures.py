
# Examples of Python control structures
# Demonstrates if, elif, else, for loops, while loops, break, continue, and pass.


# 1. Conditional Statements (if, elif, else)
# --------------------------------------------------------------------------------------------------------
    # Used to execute code only if certain conditions are met

    age = 20

    print("Conditional Statements:")

    if age < 18:
        print("You are a minor.")
    elif 18 <= age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")

    # Explanation:
    # - if: checks the first condition
    # - elif: checks additional conditions if previous ones are False
    # - else: executes if all previous conditions are False

# 2. For Loops
# --------------------------------------------------------------------------------------------------------
# Used to iterate over a sequence (like list, tuple, string)

print("For Loops:")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("Fruit:", fruit)

# Using range()
for i in range(5):  # 0 to 4
    print("Number:", i)

# Using Both
for i in range(3):  # 0 to 4
    print("Number:", fruits[i])

# 3. While Loops
# --------------------------------------------------------------------------------------------------------
# Repeats a block of code while a condition is True

print("While Loops:")

count = 0
while count < 5:
    print("Count:", count)
    count += 1  # Increment to avoid infinite loop
print("-" * 30)

# 4. Break Statement
# --------------------------------------------------------------------------------------------------------
# Terminates the loop immediately

print("Break Statement Example:")

for i in range(10):
    if i == 3:
        print("Breaking loop at i =", i)
        break  # Exit the loop
    print("i =", i)
print("-" * 30)

# 5. Continue Statement
# --------------------------------------------------------------------------------------------------------
# Skips the current iteration and moves to the next

print("Continue Statement Example:")

for i in range(5):
    if i == 2:
        print("Skipping iteration at i =", i)
        continue  # Skip this iteration
    print("i =", i)
print("-" * 30)

# 6. Pass Statement
# --------------------------------------------------------------------------------------------------------
# Placeholder statement; does nothing but syntactically required

print("Pass Statement Example:")

for i in range(3):
    if i == 1:
        pass  # Placeholder for future code
    print("i =", i)
print("-" * 30)

# 7. Nested Loops and Conditionals
# --------------------------------------------------------------------------------------------------------
# Loops inside loops and combined with conditionals

print("Nested Loops and Conditionals:")

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print(f"i ({i}) equals j ({j})")
        else:
            print(f"i ({i}) not equal to j ({j})")
print("-" * 30)

# 8. Practical Example
# --------------------------------------------------------------------------------------------------------
# Combining loops and conditionals to process a list

numbers = [5, 8, 0, 12, -3]

for num in numbers:
    if num < 0:
        print(f"{num} is negative, skipping")
        continue  # Skip negative numbers
    elif num == 0:
        print(f"{num} is zero, stopping")
        break    # Stop if zero is found
    else:
        print(f"{num} is positive")
