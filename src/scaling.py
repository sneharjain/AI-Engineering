"""
Notebook 3 - Scaling & Normalization
IIT Kharagpur AI Engineering Bootcamp

Purpose:
- Perform Min-Max Normalization.
- Perform Z-Score Standardization.
- Save scaled dataset.
- Load scaled dataset into MySQL.
"""

# --------------------------------------------------------
# Step 1 : Import Required Libraries
# --------------------------------------------------------

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

import sys
from pathlib import Path

# Add project root so database module can be imported
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from database.mysql_loader import load_to_mysql

# --------------------------------------------------------
# Step 2 : Create Sample Dataset
# --------------------------------------------------------

scaled_df = pd.DataFrame({
    "amount": [1200, 450, 980, 300, 1800, 650]
})

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)
print(scaled_df)

# --------------------------------------------------------
# Step 3 : Min-Max Normalization
# --------------------------------------------------------

minmax_scaler = MinMaxScaler()

scaled_df["amount_minmax"] = minmax_scaler.fit_transform(
    scaled_df[["amount"]]
)

print("\n" + "=" * 60)
print("MIN-MAX NORMALIZATION RESULT")
print("=" * 60)
print(scaled_df)

# --------------------------------------------------------
# Step 4 : Z-Score Standardization
# --------------------------------------------------------

standard_scaler = StandardScaler()

scaled_df["amount_standardized"] = standard_scaler.fit_transform(
    scaled_df[["amount"]]
)

print("\n" + "=" * 60)
print("Z-SCORE STANDARDIZATION RESULT")
print("=" * 60)
print(scaled_df)

# --------------------------------------------------------
# Step 5 : Save Scaled Dataset
# --------------------------------------------------------

output_path = "output/scaled_orders.csv"

scaled_df.to_csv(output_path, index=False)

print("\nScaled dataset saved successfully!")
print(f"Location : {output_path}")

# --------------------------------------------------------
# Step 6 : Load into MySQL
# --------------------------------------------------------

load_to_mysql(scaled_df, "scaled_orders")

print("\nScaling Pipeline Completed Successfully!")