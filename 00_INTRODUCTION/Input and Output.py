# This section covers basic ways to interact with users via input,
# and how to read/write files safely in Python.

# 1. Using input()
# --------------------------------------------------------------------------------------------------------
    # input() allows the user to provide data via the console.

    name = input("Enter your name: ")  # Read string input
    print("Hello,", name)

    age = input("Enter your age: ")    # input() always returns a string
    age = int(age)                      # Convert to integer
    print(f"{name} is {age} years old")

# 2. Writing to a file (text mode)
# --------------------------------------------------------------------------------------------------------
    # You can open a file in write ('w') mode to write data.
    # If the file does not exist, it is created.
    # If it exists, it is overwritten.

    file_path = "example.txt"  # Relative path (file will be created in current working directory)

    file = open(file_path, "w")  # Open file for writing
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.close()  # Always close the file to save changes
    print(f"Data written to {file_path}")

# 3. Reading from a file
# --------------------------------------------------------------------------------------------------------
    # Open a file in read ('r') mode and read its content.

    file = open(file_path, "r")  # Open file for reading
    content = file.read()         # Read entire content
    file.close()                  # Close the file
    print("File content:\n", content)

# 4. Using 'with' statement (recommended)
# --------------------------------------------------------------------------------------------------------
    # 'with' automatically closes the file even if errors occur.

    with open("example.txt", "w") as f:
        f.write("This is a safer way to write files.\n")

    with open("example.txt", "r") as f:
        print("Reading with 'with':\n", f.read())

# 5. Absolute vs Relative Paths
# --------------------------------------------------------------------------------------------------------
    # Relative paths are relative to the current working directory.
    # Use os.getcwd() to check it.

    import os
    print("Current working directory:", os.getcwd())

    # Absolute path example (Windows)
    # file_path = "C:/Users/Jose/Documents/example.txt"

    # Absolute path example (Linux/macOS)
    # file_path = "/home/jose/example.txt"

    # Using subfolders
    # file_path = "data/example.txt"  # Look inside a 'data' folder in the current directory