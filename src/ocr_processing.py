"""
Notebook 3 - OCR Processing
IIT Kharagpur AI Engineering Bootcamp

Purpose:
- Read invoice image.
- Extract text using Tesseract OCR.
- Clean OCR text.
- Extract invoice details.
- Save OCR text and load structured data into MySQL.
"""

# --------------------------------------------------------
# Step 1 : Import Required Libraries
# --------------------------------------------------------

from PIL import Image
import pytesseract
import pandas as pd
import re

import sys
from pathlib import Path

# Add project root so we can import database module
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from database.mysql_loader import load_to_mysql

# --------------------------------------------------------
# Step 2 : Configure Tesseract Path (Windows)
# --------------------------------------------------------

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# --------------------------------------------------------
# Step 3 : Read Invoice Image
# --------------------------------------------------------

image = Image.open("data/invoice_sample.png")

print("=" * 60)
print("INVOICE IMAGE LOADED")
print("=" * 60)
print(image)

# image.show()   # Optional

# --------------------------------------------------------
# Step 4 : Extract Text Using OCR
# --------------------------------------------------------

text = pytesseract.image_to_string(image)

print("\n" + "=" * 60)
print("RAW OCR OUTPUT")
print("=" * 60)
print(text)

# --------------------------------------------------------
# Step 5 : Save OCR Output
# --------------------------------------------------------

with open("output/invoice_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nOCR text saved successfully!")
print("Location : output/invoice_text.txt")

# --------------------------------------------------------
# Step 6 : Clean OCR Text
# --------------------------------------------------------

def clean_ocr_text(text):
    text = text.lower()

    # Remove special characters except numbers and ₹
    text = re.sub(r"[^\w\s₹.]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


clean_text = clean_ocr_text(text)

print("\n" + "=" * 60)
print("CLEAN OCR TEXT")
print("=" * 60)
print(clean_text)

# --------------------------------------------------------
# Step 7 : Extract Invoice Information
# --------------------------------------------------------

known_stores = [
    "morrisons",
    "walmart",
    "tesco",
    "dmart",
    "reliance",
    "fresh mart"
]

store_name = "Unknown"

for store in known_stores:
    if store in clean_text:
        store_name = store.title()
        break

# Extract total amount (supports 1460 -> 14.60)
match = re.search(r"total\s+(\d+)(\d{2})", clean_text)

if match:
    total_amount = float(match.group(1) + "." + match.group(2))
else:
    total_amount = None

print("\nExtracted Information")
print(f"Store Name   : {store_name}")
print(f"Total Amount : {total_amount}")

# --------------------------------------------------------
# Step 8 : Create OCR DataFrame
# --------------------------------------------------------

invoice_df = pd.DataFrame({
    "store_name": [store_name],
    "total_amount": [total_amount],
    "raw_text": [clean_text]
})

print("\n" + "=" * 60)
print("STRUCTURED OCR DATA")
print("=" * 60)
print(invoice_df)

# --------------------------------------------------------
# Step 9 : Load into MySQL (Reusable Loader)
# --------------------------------------------------------

load_to_mysql(invoice_df, "ocr_invoice_data")

print("\nOCR Processing Pipeline Completed Successfully!")