# Importar librerías
import pandas as pd
import numpy as np
import pyspark
import requests

# Comprobar versiones
print("Pandas version:", pd.__version__)
print("Numpy version:", np.__version__)
print("PySpark version:", pyspark.__version__)

# Crear un DataFrame de prueba con pandas
df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Jose"],
    "Edad": [25, 30, 28]
})
print("\nDataFrame de prueba:")
print(df)

# Crear un array de Numpy
arr = np.array([1, 2, 3, 4])
print("\nArray de Numpy:", arr)

# Petición HTTP de prueba
response = requests.get("https://api.github.com")
print("\nEstado de la petición a GitHub API:", response.status_code)

