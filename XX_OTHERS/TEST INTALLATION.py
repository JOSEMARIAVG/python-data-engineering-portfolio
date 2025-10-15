# Import libraries
import pandas as pd
import numpy as np
import pyspark
import requests

# Check library versions
print("Pandas version:", pd.__version__)
print("Numpy version:", np.__version__)
print("PySpark version:", pyspark.__version__)

# Create a test DataFrame with pandas
df = pd.DataFrame({
    "Name": ["Ana", "Luis", "Jose"],
    "Age": [25, 30, 28]
})
print("\nTest DataFrame:")
print(df)

# Create a Numpy array
arr = np.array([1, 2, 3, 4])
print("\nNumpy array:", arr)

# Test HTTP request
response = requests.get("https://api.github.com")
print("\nGitHub API request status:", response.status_code)