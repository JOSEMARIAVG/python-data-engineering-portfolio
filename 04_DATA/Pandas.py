# This script demonstrates advanced Pandas techniques:
# - Series and DataFrame creation and manipulation
# - Joins and merges (inner, left, right, outer)
# - Cleaning data: missing values, duplicates, type conversions
# - Transformations and aggregations (groupby, apply, map)
# - Pivot tables and reshaping
# - Performance tips for large datasets

import pandas as pd
import numpy as np

# 1. SERIES
# --------------------------------------------------------------------------------------------------------
    # A Series is a 1-dimensional labeled array.
    # Useful for quick operations on single columns.

    sales = pd.Series([100, 200, 300, 400], index=['Jan', 'Feb', 'Mar', 'Apr'])
    print("Series:")
    print(sales)

    # Access by label
    print("Sales in Feb:", sales['Feb'])

    # Access by position
    print("First element:", sales.iloc[0])

    # Vectorized operations
    print("Sales doubled:")
    print(sales * 2)

# 2. DATAFRAMES
# --------------------------------------------------------------------------------------------------------
    # A DataFrame is a 2-dimensional labeled structure, like a SQL table.

    data = {
        'customer_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'sales': [250, 150, 400, np.nan, 300],   # Notice one NaN value
        'region': ['North', 'South', 'East', 'West', 'North']
    }

    df = pd.DataFrame(data)
    print("\nDataFrame:")
    print(df)

    # Accessing columns
    print("Sales column:")
    print(df['sales'])

    # Accessing rows
    print("First row:")
    print(df.iloc[0])

    # Access subset of rows and columns
    print("Subset:")
    print(df.loc[0:2, ['name', 'sales']])

# 3. CLEANING DATA
# --------------------------------------------------------------------------------------------------------
    # Handling missing values
    print("\nMissing values in DataFrame:")
    print(df.isnull())
    print(df.isnull().sum())

    # Fill missing sales with mean
    df['sales'].fillna(df['sales'].mean(), inplace=True) # Without inplace=True, you need to replace the values manually
    print("\nDataFrame after filling NaN with mean:")
    print(df)

    # Remove duplicates
    df = pd.concat([df, df.iloc[2:3]])   # Add a duplicate row for demo
    print("\nDataFrame with duplicate added:")
    print(df)

    df.drop_duplicates(inplace=True)
    print("\nDataFrame after dropping duplicates:")
    print(df)

    # Type conversion
    df['customer_id'] = df['customer_id'].astype(str)
    print("\nData types after conversion:")
    print(df.dtypes)

# --------------------------------------------------------------------------------------------------------
# 4. JOINS / MERGES
# --------------------------------------------------------------------------------------------------------
    # Like SQL joins: combine DataFrames based on a key

    orders = pd.DataFrame({
        'order_id': [101, 102, 103, 104],
        'customer_id': ['1', '2', '2', '3'],
        'amount': [250, 150, 200, 400]
    })

    # INNER JOIN: only matching keys
    inner_join = pd.merge(df, orders, on='customer_id', how='inner')
    print("\nINNER JOIN result:")
    print(inner_join)

    # LEFT JOIN: keep all rows from left
    left_join = pd.merge(df, orders, on='customer_id', how='left')
    print("\nLEFT JOIN result:")
    print(left_join)

# 5. TRANSFORMATIONS AND AGGREGATIONS
# --------------------------------------------------------------------------------------------------------
    # Map and apply for custom transformations

    # Add a new column using map
    df['region_upper'] = df['region'].map(str.upper)
    print("\nDataFrame with region_upper column:")
    print(df)

    # Apply a custom function to sales column
    df['sales_tax'] = df['sales'].apply(lambda x: x * 0.21)
    print("\nDataFrame with sales_tax column:")
    print(df)

    # GroupBy aggregations
    grouped = df.groupby('region').agg(
        total_sales=('sales', 'sum'),
        avg_sales=('sales', 'mean'),
        count=('customer_id', 'count')
    ).reset_index() # Convert the current index into a normal column and create a standard numeric index
    print("\nAggregated sales by region:")
    print(grouped)

    # total_sales=('sales', 'sum'),             # sum → total of all values in the group
    # avg_sales=('sales', 'mean'),              # mean → average of the values
    # median_sales=('sales', 'median'),         # median → middle value of the group
    # min_sales=('sales', 'min'),               # min → smallest value in the group
    # max_sales=('sales', 'max'),               # max → largest value in the group
    # sales_std=('sales', 'std'),               # std → standard deviation
    # sales_var=('sales', 'var'),               # var → variance
    # unique_customers=('customer_id', 'nunique'), # nunique → number of unique values
    # total_customers=('customer_id', 'count'), # count → total number of rows in group
    # first_value=('sales', 'first'),           # first → first value in the group
    # last_value=('sales', 'last'),             # last → last value in the group
    # product_sales=('sales', 'prod'),          # prod → product of all values in the group
    # sales_range=('sales', lambda x: x.max() - x.min()) # custom function → range

# 6. PIVOT TABLES AND RESHAPING
# --------------------------------------------------------------------------------------------------------
    # Pivot data like Excel pivot tables
    pivot = df.pivot_table(
        index='region',
        values='sales',
        aggfunc=['sum', 'mean']
    )
    print("\nPivot table of sales by region:")
    print(pivot)

    # Melt / unpivot
    melted = df.melt(id_vars=['customer_id', 'name'], value_vars=['sales', 'sales_tax'])
    print("\nMelted DataFrame:")
    print(melted)

# 7. PERFORMANCE TIPS (continued)
# --------------------------------------------------------------------------------------------------------

    # 7.1 Use vectorized operations instead of Python loops
    # Avoid iterating row by row with df.iterrows() for large datasets.
    # Example: instead of
    df['sales_with_discount_loop'] = 0
    for i, row in df.iterrows():
        df.at[i, 'sales_with_discount_loop'] = row['sales'] * 0.9
    # .at[] is like .loc[] but faster when you want to access or modify a single cell.
    # at[ row_label, colum_label (new or existing one)]

    # Use vectorized operation (much faster)
    df['sales_with_discount'] = df['sales'] * 0.9
    print("\nVectorized sales_with_discount column:")
    print(df[['sales', 'sales_with_discount']])

    # 7.2 Reduce memory usage by converting types
    df['customer_id'] = df['customer_id'].astype('int32')  # smaller integer type
    df['region'] = df['region'].astype('category')        # categorical type saves memory
    print("\nData types after optimization:")
    print(df.dtypes)

    # 7.3 Reading large CSVs in chunks
    # Useful for datasets too large to fit into memory
    # Example:
    # for chunk in pd.read_csv('large_file.csv', chunksize=100000):
    #     process(chunk)  # process each chunk separately

    # 7.4 Use query and eval for faster filtering and calculations
    # Example: filtering with query (faster than df[df['sales']>200])
    filtered = df.query('sales > 200')
    print("\nFiltered DataFrame with sales > 200:")
    print(filtered)

    # 7.5 Working with datetime efficiently
    df['order_date'] = pd.to_datetime(['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'])
    df['month'] = df['order_date'].dt.month
    print("\nDataFrame with month extracted from order_date:")
    print(df[['order_date', 'month']])

    # 7.6 Rolling and window functions (like SQL)
    df['rolling_sales_3'] = df['sales'].rolling(window=3).mean() # Calculate a 3-period rolling average (moving average) of the 'sales' column.
    print("\nRolling 3-period average of sales:")                # This smooths short term fluctuations and highlights longer term trends by
    print(df[['sales', 'rolling_sales_3']])                      # averaging each value with the two previous ones.

    # 7.7 Multi-indexing (useful for hierarchical data)
    df_multi = df.set_index(['region', 'customer_id'])
    print("\nDataFrame with MultiIndex:")
    print(df_multi)

    # 7.8 Sorting for faster operations
    df.sort_values(by=['region', 'sales'], ascending=[True, False], inplace=True) # Sort the DataFrame by 'region' (ascending) and then by 'sales' (descending).
    print("\nDataFrame sorted by region and sales descending:")                   # This helps to organize data for analysis or reporting, showing the highest sales first within each region.
    print(df[['customer_id','region','sales']])


    # 7.9 Combining large datasets efficiently
    # Use concat for stacking datasets vertically, merge for horizontal joins
    df_large = pd.concat([df]*1000, ignore_index=True)  # simulating large dataset
    print("\nSimulated large DataFrame shape:", df_large.shape)

# 8. ADVANCED TECHNIQUES
# --------------------------------------------------------------------------------------------------------
    # This section covers advanced Pandas functionality that is essential for Data Engineers / Analysts:
    # - Categorical data optimization
    # - String manipulation and cleaning
    # - Boolean indexing and filtering
    # - Advanced datetime handling
    # - Ranking, cumulative operations, and window functions
    # - Method chaining and reshaping large datasets efficiently

    # 8.1 CATEGORICAL DATA
    # Converting string columns to category type saves memory and allows ordering
    df['region'] = df['region'].astype('category')
    df['region_ordered'] = df['region'].cat.reorder_categories(['North','South','East','West'], ordered=True)
    print("\nCategorical region column:")
    print(df[['region','region_ordered']])

    # Access category codes (numeric representation)
    df['region_code'] = df['region'].cat.codes
    print("\nRegion codes:")
    print(df[['region','region_code']])

    # 8.2 STRING MANIPULATION
    # Cleaning textual data
    df['name_clean'] = df['name'].str.strip().str.upper() #strip() function is a string method that removes whitespace (or specific characters you define) from both the beginning and the end of a string.
    df['name_length'] = df['name'].str.len()
    print("\nCleaned and measured names:")
    print(df[['name','name_clean','name_length']])

    # 8.3 BOOLEAN INDEXING AND FILTERING
    # Filter rows using multiple conditions
    high_sales_north = df[(df['sales'] > 200) & (df['region'] == 'North')]
    print("\nHigh sales in North region:")
    print(high_sales_north)

    # 8.4 ADVANCED DATETIME HANDLING
    # Create datetime column and extract components
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['weekday'] = df['order_date'].dt.day_name()
    print("\nDatetime components extracted:")
    print(df[['order_date','year','month','weekday']])

    # Resample sales by month (time series aggregation)
    df_ts = df.set_index('order_date').resample('M')['sales'].sum()
        # Convert 'order_date' to the DataFrame index and then resample the data by month ('M').
        # The resample() method groups the data based on a time frequency, in this example by monthly.
        # ['sales'].sum() aggregates the total sales within each month.
        # This operation is commonly used for time series analysis to observe monthly trends or patterns.
    print("\nMonthly sales resampled:")
    print(df_ts)

    # 8.5 RANKING AND CUMULATIVE OPERATIONS
    # Ranking customers by sales
    df['sales_rank'] = df['sales'].rank(ascending=False)
    # Cumulative sum and product
    df['cum_sales'] = df['sales'].cumsum()
    df['cum_sales_prod'] = df['sales'].cumprod()
    print("\nSales ranking and cumulative operations:")
    print(df[['customer_id','sales','sales_rank','cum_sales','cum_sales_prod']])

    # 8.6 ADVANCED PIVOTING AND RESHAPING
    # Pivot table with multiple indices and aggregation functions
    pivot_adv = df.pivot_table(
        index=['region','month'],
        values='sales',
        aggfunc=['sum','mean','count'],
        fill_value=0
    )
    print("\nAdvanced pivot table:")
    print(pivot_adv)

    # Melt/unpivot for long-format datasets
    melted_adv = df.melt(
        id_vars=['customer_id','name'],
        value_vars=['sales','sales_tax','cum_sales'],
        var_name='metric',
        value_name='value'
    )
    print("\nMelted long format DataFrame:")
    print(melted_adv.head()) 

    # 8.7 METHOD CHAINING
    # Efficient way to combine multiple operations
    data = {
        'customer_id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'sales': [250, 150, 400, np.nan, 300],   # Notice one NaN value
        'region': ['North', 'South', 'East', 'West', 'North']
    }

    df = pd.DataFrame(data)

    df_cleaned = (
        df.drop_duplicates()
        .fillna(0)
        .assign(sales_with_tax=lambda x: x['sales']*1.21)
        .query('sales > 200')
        .sort_values(by='sales', ascending=False)
    )
    print("\nCleaned DataFrame using method chaining:")
    print(df_cleaned)

    # 8.8 MEMORY AND PERFORMANCE PROFILING
    # Check memory usage
    print("\nMemory usage of DataFrame:")
    print(df_cleaned.info(memory_usage='deep'))

    # Tips for large datasets:
    # - Use categorical types for string columns
    # - Downcast numerical types
    # - Read CSVs with usecols and dtype specified
    # - Process data in chunks with chunksize parameter