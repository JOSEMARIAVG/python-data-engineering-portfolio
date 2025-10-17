# This script demonstrates:
# 1. Extract: read CSV, Excel, JSON
# 2. Transform: cleaning, filling missing values, type conversion, new calculated columns
# 3. Load: save processed individual files
# 4. Combine all three sources into a single final file

import pandas as pd
import numpy as np

# 0. CREATE EXAMPLE FILES
# --------------------------------------------------------------------------------------------------------
    data = {
        'order_id': [1, 2, 3, 4, 5, 6, 7],
        'customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'amount': [250, 150, 400, 300, np.nan, 500, 120],
        'region': ['North', 'South', 'East', 'West', 'North', 'East', 'South'],
        'date': pd.date_range(start='2025-01-01', periods=7, freq='D')
    }

    df_example = pd.DataFrame(data)
    df_example.to_csv('sales.csv', index=False)
    df_example.to_excel('sales.xlsx', index=False) # Need to install openpyxl in the cmd with your venv activated: pip install openpyxl
    df_example.to_json('sales.json', orient='records', lines=True)

    print("Example files created: sales.csv, sales.xlsx, sales.json")

# 1. PROCESS CSV
# --------------------------------------------------------------------------------------------------------
    df_csv = pd.read_csv('sales.csv')

    # Fill missing amount with mean
    df_csv['amount'].fillna(df_csv['amount'].mean(), inplace=True)

    # Add calculated columns
    df_csv['tax'] = df_csv['amount'] * 0.21
    df_csv['total'] = df_csv['amount'] + df_csv['tax']

    # Categorize region
    df_csv['market_type'] = df_csv['region'].apply(lambda r: 'Domestic' if r in ['North','East'] else 'International')

    df_csv['origin'] = 'csv'

    # Save processed CSV
    df_csv.to_csv('processed_sales_csv.csv', index=False)
    print("\nProcessed CSV saved: processed_sales_csv.csv")

# 2. PROCESS EXCEL
# --------------------------------------------------------------------------------------------------------
    df_excel = pd.read_excel('sales.xlsx')

    # Fill missing amount with mean
    df_excel['amount'].fillna(df_excel['amount'].mean(), inplace=True)

    # Add calculated columns
    df_excel['tax'] = df_excel['amount'] * 0.21
    df_excel['total'] = df_excel['amount'] + df_excel['tax']

    # Categorize region
    df_excel['market_type'] = df_excel['region'].apply(lambda r: 'Domestic' if r in ['North','East'] else 'International')

    df_excel['origin'] = 'excel'

    # Save processed Excel
    df_excel.to_excel('processed_sales_excel.xlsx', index=False)
    print("Processed Excel saved: processed_sales_excel.xlsx")

# 3. PROCESS JSON
# --------------------------------------------------------------------------------------------------------
    df_json = pd.read_json('sales.json', orient='records', lines=True)

    # Fill missing amount with mean
    df_json['amount'].fillna(df_json['amount'].mean(), inplace=True)

    # Add calculated columns
    df_json['tax'] = df_json['amount'] * 0.21
    df_json['total'] = df_json['amount'] + df_json['tax']

    # Categorize region
    df_json['market_type'] = df_json['region'].apply(lambda r: 'Domestic' if r in ['North','East'] else 'International')

    df_json['origin'] = 'json'

    # Save processed JSON
    df_json.to_json('processed_sales_json.json', orient='records', lines=True)
    print("Processed JSON saved: processed_sales_json.json")

# 4. COMBINE ALL THREE SOURCES INTO FINAL FILE
# --------------------------------------------------------------------------------------------------------
# Concatenate the three processed DataFrames
    combined_df = pd.concat([df_csv, df_excel, df_json], ignore_index=True)

    # Optional: remove duplicates in case there is overlap
    combined_df.drop_duplicates(inplace=True)

    # Save final combined file
    combined_df.to_csv('final_combined_sales.csv', index=False)
    print("\nFinal combined file saved: final_combined_sales.csv")