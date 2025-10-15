# Description: Examples of basic Python operators
# This script demonstrates arithmetic, comparison, logical,
# assignment, and bitwise operators with explanatory comments.

# 1. Arithmetic Operators
# --------------------------------------------------------------------------------------------------------
    # Used to perform basic math operations

    a = 10
    b = 3

    print("Arithmetic Operators:")
    print("a + b =", a + b)    # Addition
    print("a - b =", a - b)    # Subtraction
    print("a * b =", a * b)    # Multiplication
    print("a / b =", a / b)    # Division (returns float)
    print("a // b =", a // b)  # Floor division (integer result)
    print("a % b =", a % b)    # Modulus (remainder)
    print("a ** b =", a ** b)  # Exponentiation (a raised to the power of b)


# 2. Comparison Operators
# --------------------------------------------------------------------------------------------------------
    # Used to compare values, returning a Boolean

    print("Comparison Operators:")
    print("a == b:", a == b)   # Equal to
    print("a != b:", a != b)   # Not equal to
    print("a > b:", a > b)     # Greater than
    print("a < b:", a < b)     # Less than
    print("a >= b:", a >= b)   # Greater than or equal
    print("a <= b:", a <= b)   # Less than or equal

# 3. Logical Operators
# --------------------------------------------------------------------------------------------------------
    # Combine Boolean values

    x = True
    y = False

    print("Logical Operators:")
    print("x and y:", x and y)  # Logical AND
    print("x or y:", x or y)    # Logical OR
    print("not x:", not x)      # Logical NOT

# 4. Assignment Operators
# --------------------------------------------------------------------------------------------------------
    # Used to assign values or update variables concisely

    c = 5
    print("Assignment Operators:")
    print("Initial c:", c)

    c += 2  # Equivalent to c = c + 2
    print("c += 2:", c)

    c -= 1  # Equivalent to c = c - 1
    print("c -= 1:", c)

    c *= 3  # Equivalent to c = c * 3
    print("c *= 3:", c)

    c /= 2  # Equivalent to c = c / 2
    print("c /= 2:", c)

    c %= 3  # Equivalent to c = c % 3
    print("c %= 3:", c)

# 5. Bitwise Operators
# --------------------------------------------------------------------------------------------------------
    # Operate at the binary level (useful in low-level programming)

    x = 6      # Binary: 110
    y = 3      # Binary: 011

    print("Bitwise Operators:")
    print("x & y:", x & y)   # AND (110 & 011 -> 010 = 2)
    print("x | y:", x | y)   # OR (110 | 011 -> 111 = 7)
    print("x ^ y:", x ^ y)   # XOR (110 ^ 011 -> 101 = 5)
    print("~x:", ~x)         # NOT (invert bits, result is -7 in two's complement)
    print("x << 1:", x << 1) # Left shift (110 -> 1100 = 12)
    print("x >> 1:", x >> 1) # Right shift (110 -> 11 = 3)

# 6. Operator Precedence
# --------------------------------------------------------------------------------------------------------
    # Python evaluates expressions in a specific order

    result = 10 + 3 * 2
    # Multiplication has higher precedence than addition
    print("10 + 3 * 2 =", result)  # 10 + (3*2) = 16

    result = (10 + 3) * 2
    # Parentheses change precedence
    print("(10 + 3) * 2 =", result)  # (10+3)*2 = 26

# 7. Practical Example
# --------------------------------------------------------------------------------------------------------
    # Combining operators
    x = 4
    y = 2
    z = 3

    # Compute a formula using different operators
    final_result = (x + y) * z / 2 - 1
    print("Practical example result:", final_result)
    # Explanation: ((4+2)*3)/2 -1 = (6*3)/2 -1 = 18/2 -1 = 9 -1 = 8