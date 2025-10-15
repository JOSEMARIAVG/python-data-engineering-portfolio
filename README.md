# Python Data Engineering Portfolio

This repository contains practical examples to demonstrate my data engineering skills using **Python** and free, open-source tools.

## Projects
| Project | Description | Technologies |
|----------|--------------|---------------|
| [ETL Pipeline (API → SQLite)](notebooks/etl_example.ipynb) | Extracts, transforms, and loads data from a public API | Python, Pandas, SQLite |
| [Big Data Processing with PySpark](notebooks/pyspark_basics.ipynb) | Demonstrates data transformations using PySpark | PySpark |
| [Automated Data Pipeline](src/) | Automates ETL tasks with scheduling | Python, Cron |

## Tech Stack
- Python 3.10+
- Pandas, PySpark
- SQLite
- Requests, BeautifulSoup
- Pytest (for testing)

## Run locally
```bash
git clone https://github.com/<yourusername>/python-data-engineering-portfolio.git
cd python-data-engineering-portfolio
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
