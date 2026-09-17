"""
Notebook 3 - Data Encoding
IIT Kharagpur AI Engineering Bootcamp

Purpose:
- Perform Label Encoding.
- Perform One-Hot Encoding.
- Perform Ordinal Encoding.
- Save encoded dataset.
- Load encoded dataset into MySQL.
"""

# --------------------------------------------------------
# Step 1 : Import Required Libraries
# --------------------------------------------------------

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from database.mysql_loader import load_to_mysql

# --------------------------------------------------------
# Step 2 : Create Sample Dataset
# --------------------------------------------------------

orders_df = pd.DataFrame({
    "customer": ["Sneha", "Rahul", "Priya", "Amit", "Sneha"],
    "city": ["Bangalore", "Delhi", "Mumbai", "Delhi", "Bangalore"],
    "transaction_category": [
        "High Value",
        "Low Value",
        "Medium Value",
        "Low Value",
        "High Value"
    ]
})

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)
print(orders_df)

# --------------------------------------------------------
# Step 3 : Label Encoding
# --------------------------------------------------------

encoder = LabelEncoder()

orders_df["category_encoded"] = encoder.fit_transform(
    orders_df["transaction_category"]
)

print("\n" + "=" * 60)
print("LABEL ENCODING RESULT")
print("=" * 60)
print(orders_df)

print("\nLabel Encoding Mapping")
for category, value in zip(
    encoder.classes_,
    encoder.transform(encoder.classes_)
):
    print(f"{category} --> {value}")

# --------------------------------------------------------
# Step 4 : One-Hot Encoding
# --------------------------------------------------------

encoded_df = pd.get_dummies(
    orders_df,
    columns=["city"],
    dtype=int
)

print("\n" + "=" * 60)
print("ONE-HOT ENCODING RESULT")
print("=" * 60)
print(encoded_df)

# --------------------------------------------------------
# Step 5 : Ordinal Encoding
# --------------------------------------------------------

education_df = pd.DataFrame({
    "education": [
        "Graduate",
        "School",
        "Post Graduate",
        "Graduate"
    ]
})

education_mapping = {
    "School": 0,
    "Graduate": 1,
    "Post Graduate": 2
}

education_df["education_encoded"] = education_df["education"].map(
    education_mapping
)

print("\n" + "=" * 60)
print("ORDINAL ENCODING RESULT")
print("=" * 60)
print(education_df)

# --------------------------------------------------------
# Step 6 : Save Encoded Dataset
# --------------------------------------------------------

encoded_df.to_csv("output/encoded_orders.csv", index=False)

print("\nEncoded dataset saved successfully!")
print("Location : output/encoded_orders.csv")

# --------------------------------------------------------
# Step 7 : Load Encoded Dataset into MySQL
# --------------------------------------------------------

load_to_mysql(encoded_df, "encoded_orders")