import pandas as pd
import numpy as np
import sqlite3
import re
import string
from datetime import datetime #used for parsing dates
from dateutil import parser as dateparser # used for parsing dates

from nltk.stem import PorterStemmer #used for stemming words

import matplotlib.pyplot as plt # used for plotting graphs

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)

print("Setup complete — all libraries imported successfully.")

# --- Create a raw, messy dataset (simulating a real extracted export) ---
raw_data = {
    "id":     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name":   ["A. Rao", "", "b khan", "C. Iyer", "d. patel", "A. Rao", "E. Menon", "", "F. Das", "b khan"],
    "amount": ["1200", "-", "980", "NaN", "450", "1200", "-75", "300", "NaN", "980"],
    "date":   ["2026-01-04", "2026/01/05", "04-01-2026", "", "2026-01-06", "2026-01-04",
               "07-01-2026", "2026/01/07", "2026-01-08", "04-01-2026"],
}
raw_df = pd.DataFrame(raw_data) #convert the dictionary to a pandas DataFrame or table
raw_df.to_csv("data/raw_orders.csv", index=False) # save the dataframe to a CSV file

print("Raw CSV saved as 'raw_orders.csv'")
print(raw_df)

# Step 1 — Extract 
# Read the raw CSV exactly as it exists, with no modifications.

extracted_df = pd.read_csv("data/raw_orders.csv") # read the CSV file into a pandas DataFrame
print(f"Extracted {len(extracted_df)} rows.")
print (extracted_df.dtypes) # to check the data types of each column

## Step 2 — Transform

## Clean and standardize the extracted data:
## - Fill missing names with `"Unknown"` and standardize casing
## - Parse every date format into a single standard format (`YYYY-MM-DD`)
## - Convert `amount` to numeric, treating invalid/negative values as `0`
## - Remove duplicate records (same name + date + amount)

def clean_name(name):
    if pd.isna(name) or str(name).strip() == "":
        return "Unknown"
    return str(name).strip().title().replace(".", "")

def parse_any_date(value):
    if pd.isna(value) or str(value).strip() == "":
        return pd.NaT
    try:
        return dateparser.parse(str(value), dayfirst=False, yearfirst=True)
    except (ValueError, TypeError):
        return pd.NaT

def clean_amount(value):
    try:
        num = float(value)
        return num if num > 0 else 0.0
    except (ValueError, TypeError):
        return 0.0

transformed_df = extracted_df.copy()
transformed_df["name"] = transformed_df["name"].apply(clean_name)
transformed_df["date"] = transformed_df["date"].apply(parse_any_date).dt.strftime("%Y-%m-%d")
transformed_df["amount"] = transformed_df["amount"].apply(clean_amount)

before_dedupe = len(transformed_df)
transformed_df = transformed_df.drop_duplicates(subset=["name", "date", "amount"]).reset_index(drop=True)
after_dedupe = len(transformed_df)

print(f"Rows before de-duplication: {before_dedupe}")
print(f"Rows after de-duplication:  {after_dedupe}  ({before_dedupe - after_dedupe} duplicate(s) removed)")
print(transformed_df)


## Step 3 — Load
## Write the cleaned data to a new CSV **and** load it into a MySql table.

from sqlalchemy import create_engine, text

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:AiBootcamp%402026@localhost:3307/ai_engineering_db"
)

# Load DataFrame into MySQL table
transformed_df.to_sql(
    name="clean_orders",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Clean data saved to MySQL table 'clean_orders'.")

# Verify the data
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM clean_orders LIMIT 5"))

    print("\nFirst 5 rows from MySQL:")
    for row in result:
        print(row)
