# AI Data Engineering ETL Pipeline

A complete **Extract → Transform → Load (ETL)** pipeline built as part of the **IIT Kharagpur Generative AI & Agentic AI Bootcamp**.

This project demonstrates how raw, messy datasets are cleaned, transformed, enriched, and loaded into **MySQL** using Python.

---

## Project Overview

This project simulates a real-world AI data engineering workflow.

The pipeline performs:

* Data Extraction from CSV files.
* Data Cleaning and Validation.
* Feature Engineering.
* Text Processing (NLP).
* OCR Processing using Tesseract.
* Data Encoding.
* Scaling & Normalization.
* Loading processed datasets into MySQL.

The project follows ETL best practices and stores intermediate datasets in an **output** folder.

---

## Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python 3.11  | Programming Language |
| Pandas       | Data Processing      |
| NumPy        | Numerical Operations |
| Scikit-learn | Encoding & Scaling   |
| NLTK         | Text Processing      |
| Pillow       | Image Processing     |
| PyTesseract  | OCR Extraction       |
| SQLAlchemy   | MySQL Integration    |
| PyMySQL      | MySQL Connector      |
| MySQL 8.0    | Database             |

---

## Project Structure

AI-Engineering/

├── data/                  # Raw datasets and images

│   ├── raw_orders.csv

│   ├── reviews.csv

│   ├── invoice_sample.png

│

├── output/                # Processed datasets

│   ├── clean_orders.csv

│   ├── feature_orders.csv

│   ├── encoded_orders.csv

│   ├── scaled_orders.csv

│   ├── processed_reviews.csv

│   └── invoice_text.txt

│

├── database/              # Reusable MySQL utilities

│   ├── **init**.py

│   ├── mysql_loader.py

│   └── aiDb.sql

│

├── src/                   # ETL pipeline scripts

│   ├── extract.py

│   ├── clean_data.py

│   ├── feature_engineering.py

│   ├── text_processing.py

│   ├── ocr_processing.py

│   ├── encoding.py

│   ├── scaling.py

│   └── pipeline.py

│

├── requirements.txt

├── .gitignore

└── README.md

---

## ETL Pipeline Flow

Raw CSV / Image

↓

Extract Data

↓

Clean Data

↓

Feature Engineering

↓

Text Processing (NLP)

↓

OCR Processing

↓

Encoding

↓

Scaling & Normalization

↓

MySQL Database

---

## Features Implemented

### 1. Extract Data

* Read CSV datasets.
* Display dataset shape.
* Inspect data types.
* Detect missing values.

### 2. Data Cleaning

* Fill missing names.
* Standardize date formats.
* Clean numeric values.
* Remove duplicates.

### 3. Feature Engineering

* Extract Year, Month, Day.
* Extract Weekday.
* Create Transaction Category.
* Create Name Length Feature.

### 4. Text Processing (NLP)

* Lowercase conversion.
* Remove punctuation.
* Remove numbers.
* Tokenization.
* Stop-word removal.
* Stemming.
* Lemmatization.

### 5. OCR Processing

* Extract text from invoice images.
* Clean OCR output.
* Extract Store Name.
* Extract Total Amount.

### 6. Encoding

* Label Encoding.
* One-Hot Encoding.
* Ordinal Encoding.

### 7. Scaling

* Min-Max Normalization.
* Z-Score Standardization.

### 8. MySQL Loading

A reusable utility (`mysql_loader.py`) loads processed DataFrames into MySQL.

---

## Output Files

| File                  | Description                  |
| --------------------- | ---------------------------- |
| clean_orders.csv      | Cleaned customer orders.     |
| feature_orders.csv    | Feature engineered dataset.  |
| encoded_orders.csv    | Encoded categorical dataset. |
| scaled_orders.csv     | Normalized dataset.          |
| processed_reviews.csv | NLP processed reviews.       |
| invoice_text.txt      | OCR extracted invoice text.  |

---

## MySQL Tables Created

* clean_orders
* feature_orders
* encoded_orders
* scaled_orders
* processed_reviews
* ocr_invoice_data

---

## How to Run the Project

### Clone Repository

```bash
git clone <repository-url>
cd AI-Engineering
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment (Windows)

```powershell
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Complete Pipeline

```bash
python src/pipeline.py
```

---

## Skills Demonstrated

* ETL Pipeline Design.
* Data Cleaning Pipelines.
* Feature Engineering.
* Natural Language Processing.
* OCR using Tesseract.
* Data Encoding.
* Scaling & Normalization.
* MySQL Data Loading.
* Python Project Structure.

---

## Course Information

**Course:** IIT Kharagpur – Generative AI & Agentic AI Bootcamp

**Notebook:** Notebook 3 – Data Engineering for AI Applications

---

## Author

**Sneha Jain**

QA Test Lead | AI Engineering Learner | Playwright & Python Automation Enthusiast
