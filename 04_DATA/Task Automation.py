# This script demonstrates task automation using:
# - schedule: Python library for simple recurring tasks
# - cron jobs: OS-level scheduling (Linux/Mac) or Task Scheduler (Windows)
# - Useful for ETL, data fetching, and periodic reporting

import schedule
import time
import pandas as pd
import requests
from datetime import datetime

# --------------------------------------------------------------------------------------------------------
# 1. DEFINE A TASK FUNCTION
# --------------------------------------------------------------------------------------------------------
# A task function could be anything: fetch data from an API, clean a CSV, or run an ETL pipeline
def fetch_api_data():
    print(f"[{datetime.now()}] Running fetch_api_data task...")
    
    # Example: fetch posts from JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    
    # Convert to DataFrame and save
    df = pd.DataFrame(data)
    filename = f"posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    
    print(f"Data saved to {filename}\n")

# --------------------------------------------------------------------------------------------------------
# 2. SCHEDULE TASKS USING SCHEDULE LIBRARY
# --------------------------------------------------------------------------------------------------------
# Schedule a task to run periodically using a friendly syntax
# Examples: every minute, every 5 seconds, every hour, daily at a specific time

# Run fetch_api_data every 10 seconds (demo purpose)
schedule.every(10).seconds.do(fetch_api_data)

# Run fetch_api_data every day at 09:00
# schedule.every().day.at("09:00").do(fetch_api_data)

# Run fetch_api_data every hour
# schedule.every().hour.do(fetch_api_data)

# --------------------------------------------------------------------------------------------------------
# 3. KEEP SCHEDULER RUNNING
# --------------------------------------------------------------------------------------------------------
print("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()  # run any jobs that are scheduled to run
    time.sleep(5)           # wait 1 second before checking again

# --------------------------------------------------------------------------------------------------------
# 4. CRON JOBS (OS-level scheduling)
# --------------------------------------------------------------------------------------------------------
# Cron jobs allow running Python scripts automatically at OS level (Linux / Mac)
# Example: run every day at 9:00 AM
# 0 9 * * * /usr/bin/python3 /path/to/your/script.py

# On Windows, use Task Scheduler:
# - Create Basic Task → Trigger: Daily / Hourly → Action: Start a program → Program/script: python.exe → Add arguments: path\to\script.py

# Advantages:
# - schedule library: good for scripts running continuously in Python
# - cron jobs / Task Scheduler: good for periodic automation without keeping Python running
