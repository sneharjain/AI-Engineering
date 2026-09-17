"""
Notebook 3 - Extract Data
IIT Kharagpur AI Engineering Bootcamp

Purpose:
- Read the raw dataset.
- Understand dataset structure.
- Check columns, data types, missing values and basic statistics.
"""

# --------------------------------------------------------
# Step 1 : Import Required Library
# --------------------------------------------------------

import pandas as pd

# --------------------------------------------------------
# Step 2 : Read the Raw Dataset
# --------------------------------------------------------

orders_df = pd.read_csv("data/raw_orders.csv")

print("=" * 60)
print("RAW DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print(orders_df)

# --------------------------------------------------------
# Step 3 : Dataset Shape
# --------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print(f"Rows    : {orders_df.shape[0]}")
print(f"Columns : {orders_df.shape[1]}")

# --------------------------------------------------------
# Step 4 : Column Names
# --------------------------------------------------------

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

print(orders_df.columns.tolist())

# --------------------------------------------------------
# Step 5 : Data Types
# --------------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(orders_df.dtypes)

# --------------------------------------------------------
# Step 6 : Preview Dataset
# --------------------------------------------------------

print("\n" + "=" * 60)
print("FIRST 5 ROWS")
print("=" * 60)

print(orders_df.head())

# --------------------------------------------------------
# Step 7 : Dataset Information
# --------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

orders_df.info()

# --------------------------------------------------------
# Step 8 : Missing Values
# --------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(orders_df.isnull().sum())

# --------------------------------------------------------
# Step 9 : Basic Statistics
# --------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(orders_df.describe(include="all"))