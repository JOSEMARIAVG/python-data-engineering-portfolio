# This script demonstrates how to use NumPy for numerical computations:
# - Array creation and manipulation
# - Broadcasting and vectorized operations
# - Indexing, slicing, and filtering
# - Aggregations and mathematical operations
# - Useful functions for Data Engineers / Data Analysts

import numpy as np

# 1. ARRAY CREATION
# --------------------------------------------------------------------------------------------------------
    # NumPy arrays are homogeneous and much faster than Python lists for numerical operations.

    # From a Python list
    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)

    # Multi-dimensional array (matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2D Array (Matrix):")
    print(matrix)

    # Create arrays with zeros, ones, and random values
    zeros = np.zeros((2, 3))   # 2x3 matrix of zeros
    ones = np.ones((3, 2))     # 3x2 matrix of ones
    randoms = np.random.rand(2, 3)  # 2x3 matrix with random values in [0,1) decimal values
    print("\nZeros:\n", zeros)
    print("\nOnes:\n", ones)
    print("\nRandom values:\n", randoms)

# 2. ARRAY PROPERTIES
# --------------------------------------------------------------------------------------------------------
    print("\nArray shape:", matrix.shape)   # (2, 3)
    print("Array dimensions:", matrix.ndim) # 2
    print("Data type:", matrix.dtype)       # int32 depending on system

# 3. INDEXING AND SLICING
# --------------------------------------------------------------------------------------------------------
    # Access elements using indices (0-based)
    print("\nFirst row:", matrix[0])
    print("Element at row 2, column 3:", matrix[1, 2])

    # Slicing: [start:end:step]
    print("\nFirst two columns of all rows:")
    print(matrix[:, 0:2])

    # Boolean indexing
    mask = matrix > 3
    print("\nBoolean mask (values > 3):")
    print(mask)
    print("Filtered values:", matrix[(matrix > 3)])

# 4. VECTORIZED OPERATIONS
# --------------------------------------------------------------------------------------------------------
    # NumPy allows applying operations on entire arrays without loops (broadcasting).
    # This is much faster and memory efficient.

    arr = np.array([10, 20, 30, 40, 50])
    print("\nOriginal array:", arr)

    # Element-wise operations
    print("Array + 5:", arr + 5)
    print("Array squared:", arr ** 2)
    print("Array divided by 10:", arr / 100)

    # Broadcasting example (operations between different shapes)
    matrix_2 = np.array([[1], [2], [3]])  # shape (3,1)
    row = np.array([10, 20, 30])          # shape (3,)
    print("\nBroadcasting example (matrix_2 + row):")
    print(matrix_2 + row)  # Automatically expands shapes

# 5. AGGREGATIONS AND STATISTICS
# --------------------------------------------------------------------------------------------------------
    data = np.random.randint(1, 100, size=(5, 4))  # random integers 1–99
    print("\nData array:\n", data)

    print("Sum of all elements:", data.sum())
    print("Mean of all elements:", data.mean())
    print("Standard deviation:", data.std())
    print("Minimum value:", data.min())
    print("Maximum value:", data.max())

    # Aggregate along axes
    print("\nSum per row (axis=1):", data.sum(axis=1))
    print("Sum per column (axis=0):", data.sum(axis=0))

# 6. RESHAPING AND STACKING
# --------------------------------------------------------------------------------------------------------
    # Change the shape of an array without modifying data
    reshaped = np.arange(12).reshape(3, 4)
    print("\nReshaped 3x4 array:\n", reshaped)

    # Vertical and horizontal stacking
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print("\nVertical stack:\n", np.vstack([a, b]))
    print("Horizontal stack:\n", np.hstack([a, b]))

# 7. NUMPY USEFUL FUNCTIONS
# --------------------------------------------------------------------------------------------------------
    # Create evenly spaced numbers
    linear = np.linspace(0, 10, 5)
    print("\nLinearly spaced values:", linear)

    # Mathematical functions
    angles = np.array([0, np.pi/2, np.pi])
    print("\nSine values:", np.sin(angles))
    print("Cosine values:", np.cos(angles))

    # Random seed for reproducibility
    np.random.seed(42)
    print("\nRandom values with fixed seed:", np.random.rand(3))
    np.random.seed(42)
    print("\nRandom values with fixed seed:", np.random.rand(3))

# 8. PERFORMANCE TIP: USE VECTORIZED OPERATIONS INSTEAD OF LOOPS
# --------------------------------------------------------------------------------------------------------
    # Example: computing the square of each element

    data = np.arange(1_000_000)

    # Slow way (Python loop)
    # squares = [x**2 for x in data]

    # Fast way (NumPy vectorized)
    squares = data ** 2
    print("\nSquare vector:",squares)
    # Example of performance optimization using vectorized operations
    # Computed squares for 1 million elements instantly