
"""
Notebook 3 - Data Cleaning Pipeline
IIT Kharagpur AI Engineering Bootcamp

Purpose:
- Handle missing values.
- Standardize names.
- Standardize dates.
- Clean numeric amounts.
- Remove duplicate records.
- Save cleaned dataset to output folder.
"""

# -----------------------------
# Step 1 : Read the Raw Dataset
# -----------------------------

import pandas as pd
from dateutil import parser as dateparser

# Read raw dataset
orders_df = pd.read_csv("data/raw_orders.csv")

print("=" * 60)
print("RAW DATASET")
print("=" * 60)
print(orders_df)

# -----------------------------
# Step 2 : Create Working Copy
# -----------------------------

# Never modify the original dataframe directly.
clean_df = orders_df.copy()

print("\nWorking copy created successfully.")

# -----------------------------
# Step 3 : Handle Missing Names
# -----------------------------

def clean_name(name):
    if pd.isna(name) or str(name).strip() == "":
        return "Unknown"

    return str(name).strip().title().replace(".", "")


clean_df["name"] = clean_df["name"].apply(clean_name)

print("\nNames cleaned successfully.")
print(clean_df[["id", "name"]])

# -----------------------------
# Step 4 : Standardize Dates
# -----------------------------

def parse_any_date(value):
    if pd.isna(value) or str(value).strip() == "":
        return pd.NaT

    text = str(value).strip()

    try:
        # Handle YYYY-MM-DD or YYYY/MM/DD
        if text.startswith("2026"):
            return dateparser.parse(text, yearfirst=True)

        # Handle DD-MM-YYYY
        return dateparser.parse(text, dayfirst=True)

    except (ValueError, TypeError):
        return pd.NaT


clean_df["date"] = clean_df["date"].apply(parse_any_date)
clean_df["date"] = clean_df["date"].dt.strftime("%Y-%m-%d")

print("\nDates standardized successfully.")
print(clean_df[["id", "date"]])

# -----------------------------
# Step 5 : Clean Numeric Amounts
# -----------------------------

def clean_amount(value):
    try:
        amount = float(value)

        # Handle NaN values
        if pd.isna(amount):
            return 0.0

        # Convert negative values to zero
        if amount < 0:
            return 0.0

        return amount

    except (ValueError, TypeError):
        return 0.0


clean_df["amount"] = clean_df["amount"].apply(clean_amount)

print("\nAmounts cleaned successfully.")
print(clean_df[["id", "amount"]])

# -----------------------------
# Step 6 : Remove Duplicate Records
# -----------------------------

rows_before = len(clean_df)

clean_df = clean_df.drop_duplicates(
    subset=["name", "date", "amount"]
).reset_index(drop=True)

rows_after = len(clean_df)

print("\nDuplicate records removed successfully.")
print(f"Rows before cleaning : {rows_before}")
print(f"Rows after cleaning  : {rows_after}")
print(f"Duplicates removed   : {rows_before - rows_after}")

# -----------------------------
# Step 7 : Final Missing Value Cleanup
# -----------------------------

clean_df["amount"] = clean_df["amount"].fillna(0.0)
clean_df["date"] = clean_df["date"].fillna("Unknown")

# -----------------------------
# Step 8 : Display Final Dataset
# -----------------------------

print("\n" + "=" * 60)
print("FINAL CLEAN DATASET")
print("=" * 60)
print(clean_df)

# -----------------------------
# Step 9 : Save Clean Dataset
# -----------------------------

clean_df.to_csv("output/clean_orders.csv", index=False)

print("\nClean dataset saved successfully!")
print("Location : output/clean_orders.csv")