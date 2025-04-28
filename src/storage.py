"""
Storage functions for reading and writing student data.
"""

import json
import pandas as pd
import os

DATA_DIR = 'data'
STUDENTS_JSON = os.path.join(DATA_DIR, 'students.json')
STUDENTS_CSV = os.path.join(DATA_DIR, 'students.csv')

def read_json() -> list:
    """Read student data from a JSON file."""
    if os.path.exists(STUDENTS_JSON):
        with open(STUDENTS_JSON, 'r') as f:
            return json.load(f)
    return []

def write_json(data: list):
    """Write student data to a JSON file."""
    with open(STUDENTS_JSON, 'w') as f:
        json.dump(data, f, indent=4)

def read_csv() -> pd.DataFrame:
    """Read student data from a CSV file."""
    if os.path.exists(STUDENTS_CSV):
        return pd.read_csv(STUDENTS_CSV)
    return pd.DataFrame()

def write_csv(data: pd.DataFrame):
    """Write student data to a CSV file."""
    data.to_csv(STUDENTS_CSV, index=False)

def import_initial_data(csv_file: str):
    """Import initial dataset from a CSV file."""
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        return df.to_dict(orient='records')
    return []
