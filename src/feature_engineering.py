"""
Notebook 3 - Feature Engineering
IIT Kharagpur AI Engineering Bootcamp

Purpose:
- Read cleaned dataset.
- Create date-based features.
- Create transaction categories.
- Create name length feature.
- Save engineered dataset.
- Load into MySQL.
"""

# --------------------------------------------------------
# Step 1 : Import Libraries
# --------------------------------------------------------

import pandas as pd
from sqlalchemy import create_engine
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from database.mysql_loader import load_to_mysql

# --------------------------------------------------------
# Step 2 : Read Clean Dataset
# --------------------------------------------------------

feature_df = pd.read_csv("output/clean_orders.csv")

print("=" * 60)
print("CLEAN DATASET LOADED")
print("=" * 60)
print(feature_df.head())

# --------------------------------------------------------
# Step 3 : Convert Date Column
# --------------------------------------------------------

feature_df["date"] = pd.to_datetime(
    feature_df["date"],
    errors="coerce",
    dayfirst=True
)

print("\nDate column converted successfully.")
print(feature_df["date"].head())

# --------------------------------------------------------
# Step 4 : Extract Year, Month, Day
# --------------------------------------------------------

feature_df["year"] = feature_df["date"].dt.year
feature_df["month"] = feature_df["date"].dt.month
feature_df["day"] = feature_df["date"].dt.day

print("\nDate Features")
print(feature_df[["date", "year", "month", "day"]])

# --------------------------------------------------------
# Step 5 : Extract Weekday
# --------------------------------------------------------

feature_df["weekday"] = feature_df["date"].dt.day_name()

print("\nWeekday Feature")
print(feature_df[["date", "weekday"]])

# --------------------------------------------------------
# Step 6 : Create Transaction Category
# --------------------------------------------------------

def categorize_transaction(amount):

    if amount == 0:
        return "Invalid"

    elif amount <= 500:
        return "Low Value"

    elif amount <= 1000:
        return "Medium Value"

    else:
        return "High Value"


feature_df["transaction_category"] = feature_df["amount"].apply(
    categorize_transaction
)

print("\nTransaction Categories")
print(feature_df[["amount", "transaction_category"]])

# --------------------------------------------------------
# Step 7 : Create Name Length Feature
# --------------------------------------------------------

feature_df["name_length"] = feature_df["name"].fillna("").str.len()

print("\nName Length Feature")
print(feature_df[["name", "name_length"]])

# --------------------------------------------------------
# Step 8 : Display Final Dataset
# --------------------------------------------------------

print("\n" + "=" * 60)
print("FEATURE ENGINEERED DATASET")
print("=" * 60)

print(feature_df)

# --------------------------------------------------------
# Step 9 : Save Feature Engineered Dataset
# --------------------------------------------------------

feature_df.to_csv("output/feature_orders.csv", index=False)

print("\nFeature engineered dataset saved successfully!")
print("Location : output/feature_orders.csv")

# --------------------------------------------------------
# Step 10 : Load into MySQL
# --------------------------------------------------------

load_to_mysql(feature_df, "feature_orders")