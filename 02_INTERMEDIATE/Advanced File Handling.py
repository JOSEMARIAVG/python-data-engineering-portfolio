
# This section shows how to handle structured data files:
# - CSV files (Comma-Separated Values)
# - JSON files (JavaScript Object Notation)
# These formats are commonly used for data exchange and storage.

import csv
import json

# 1. CSV Files
# --------------------------------------------------------------------------------------------------------
    # Writing to a CSV file
    csv_data = [
        ["Name", "Age", "Country"],
        ["Jose", 27, "ESP"],
        ["Raul", 22, "UK"],
        ["Aitana", 27, "Canada"]
    ]

    csv_file_path = "people.csv"

    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)  # Write all rows at once

    # Reading from a CSV file
    with open(csv_file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print("CSV Row:", row)

# 2. JSON Files
# --------------------------------------------------------------------------------------------------------
    # JSON is widely used for APIs and configuration files

    # Data to write
    json_data = {
        "employees": [
            {"name": "Alice", "age": 10, "country": "USA"},
            {"name": "Bob", "age": 55, "country": "UK"},
            {"name": "Charlie", "age": 90, "country": "Canada"}
        ],
        "company": "TechCorp"
    }

    json_file_path = "data.json"

    # Writing JSON
    with open(json_file_path, "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)  # indent makes it human-readable

    # Reading JSON
    with open(json_file_path, "r") as jsonfile:
        data = json.load(jsonfile)
        print("Company:", data["company"])
        for emp in data["employees"]:
            print(f"{emp['name']} ({emp['age']}) from {emp['country']}")

# 3. Extra
# --------------------------------------------------------------------------------------------------------
    # - Use 'newline=""' when writing CSV files to avoid blank lines on Windows
    # - Use 'indent' in json.dump() to make the file readable
    # - CSV handles tabular data, JSON handles hierarchical/nested data
    # - Always use 'with' to ensure files are closed properly