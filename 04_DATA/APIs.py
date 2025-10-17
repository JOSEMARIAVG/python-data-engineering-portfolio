# This script demonstrates:
# - Fetching data from a public API
# - Transforming the JSON data into a Pandas DataFrame
# - Cleaning, processing, and calculating new columns
# - Saving processed data locally as CSV and JSON
# --------------------------------------------------------------------------------------------------------

import requests
import pandas as pd

# 1. EXTRACT: FETCH DATA FROM API
# --------------------------------------------------------------------------------------------------------
url = "https://fakestoreapi.com/products"

response = requests.get(url)  # Send GET request to API
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(f"Fetched {len(data)} records from API")
else:
    raise Exception(f"API request failed with status code {response.status_code}")

# 2. TRANSFORM: JSON TO DATAFRAME
# --------------------------------------------------------------------------------------------------------
df = pd.DataFrame(data)
print("\nInitial DataFrame head:")
print(df.head())
print(df.dtypes)

# Split column rating
df['rate'] = df['rating'].apply(lambda x: x['rate'])
df['count'] = df['rating'].apply(lambda x: x['count'])
del df['rating']

# Filter rows
df_filtered_not_gold = df[~df['title'].str.contains('Gold')] # Not Gold in the title
df_filtered_gold = df[df['title'].str.contains('Gold')] # Gold in the title

df_group = df_filtered_not_gold.groupby('category').agg(
    max_rate = ('rate','max'),
    min_rate = ('rate','min'),
    sum_rate = ('count','sum'),
    count = ('id','count')
).reset_index()

# 3. LOAD: SAVE DATA LOCALLY
# --------------------------------------------------------------------------------------------------------
df_group.to_csv('api_data_saved.csv', index=False)

print("\nProcessed API data saved:")
print("api_data_saved.csv")
