"""
Notebook 3 - Complete ETL Pipeline
IIT Kharagpur AI Engineering Bootcamp

Purpose:
Run the complete ETL pipeline in sequence.
"""

import runpy
from pathlib import Path

# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ETL Pipeline Steps
pipeline_steps = [
    ("STEP 1 : Extract Data", PROJECT_ROOT / "src" / "extract.py"),
    ("STEP 2 : Clean Data", PROJECT_ROOT / "src" / "clean_data.py"),
    ("STEP 3 : Feature Engineering", PROJECT_ROOT / "src" / "feature_engineering.py"),
    ("STEP 4 : Text Processing", PROJECT_ROOT / "src" / "text_processing.py"),
    ("STEP 5 : OCR Processing", PROJECT_ROOT / "src" / "ocr_processing.py"),
    ("STEP 6 : Encoding", PROJECT_ROOT / "src" / "encoding.py"),
    ("STEP 7 : Scaling & Normalization", PROJECT_ROOT / "src" / "scaling.py"),
]

print("=" * 70)
print("AI ENGINEERING ETL PIPELINE STARTED")
print("=" * 70)

# Run each script one by one
for step_name, script_path in pipeline_steps:
    print(f"\n{step_name}")
    print("-" * 70)

    try:
        runpy.run_path(str(script_path), run_name="__main__")
        print(f"✅ {step_name} Completed Successfully")

    except Exception as error:
        print(f"❌ {step_name} Failed")
        print(f"Error: {error}")
        break

print("\n" + "=" * 70)
print("ETL PIPELINE COMPLETED")
print("=" * 70)