# This script demonstrates how to connect to a database, execute queries, and interact with tables using:
# - SQLite (lightweight, file-based database)
# - SQLAlchemy (Python SQL toolkit and ORM)
# Useful for ETL pipelines, data ingestion, and data analysis workflows.

import sqlite3
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData # pip install SQLAlchemy

# 1.1 USING SQLITE DIRECTLY
# --------------------------------------------------------------------------------------------------------
    # Connect to a SQLite database (creates file if not exists)
    conn = sqlite3.connect('sales_data.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales(
        customer_id INTEGER,
        name TEXT,
        sales REAL,
        region TEXT
    )
    ''')

    # Insert sample data
    sample_data = [
        (1, 'Alice', 250, 'North'),
        (2, 'Bob', 150, 'South'),
        (3, 'Charlie', 400, 'East')
    ]
    cursor.executemany('INSERT INTO sales VALUES (?,?,?,?)', sample_data)
    conn.commit()

    # Query data into Pandas
    df_sqlite = pd.read_sql_query('SELECT * FROM sales', conn)
    print("Data read from SQLite:")
    print(df_sqlite)

    # Close connection
    conn.close()

# 1.2 USING SQLALCHEMY
# --------------------------------------------------------------------------------------------------------
    # SQLAlchemy allows higher-level operations and ORM capabilities
    engine = create_engine('sqlite:///sales_data.db', echo=False)  # echo=True shows SQL queries
    metadata = MetaData()

    # Define table structure
    sales_table = Table('sales', metadata,
                        Column('customer_id', Integer, primary_key=False),
                        Column('name', String),
                        Column('sales', Float),
                        Column('region', String)
                    )

    # Create table if not exists
    metadata.create_all(engine)

    # Insert data using Pandas
    new_data = pd.DataFrame({
        'customer_id': [4, 5],
        'name': ['David', 'Eve'],
        'sales': [300, 350],
        'region': ['West', 'North']
    })

    # Write to database (append new data)
    new_data.to_sql('sales', con=engine, if_exists='append', index=False)

    # Query with Pandas
    df_sqlalchemy = pd.read_sql('SELECT * FROM sales WHERE sales > 200', con=engine)
    print("\nData read from SQLAlchemy (sales > 200):")
    print(df_sqlalchemy)

# 1.3 EXTRA
# --------------------------------------------------------------------------------------------------------
    # - Always close connections when using sqlite3 to avoid locking the file
    # - Use SQLAlchemy for more complex pipelines and ORM features
    # - Pandas' to_sql and read_sql/read_sql_query are very convenient for ETL
    # - SQLAlchemy can connect to many database types (PostgreSQL, MySQL, SQL Server) with minimal changes
