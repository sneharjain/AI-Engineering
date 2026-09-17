"""
Notebook 3 - Text Processing (NLP)
IIT Kharagpur AI Engineering Bootcamp

Purpose:
- Clean review text.
- Tokenize words.
- Remove stop words.
- Perform stemming and lemmatization.
- Create final clean text.
- Save processed reviews.
- Load processed reviews into MySQL.
"""

# --------------------------------------------------------
# Step 1 : Import Required Libraries
# --------------------------------------------------------

import pandas as pd
import re
import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

import sys
from pathlib import Path

# Add project root for reusable MySQL loader
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from database.mysql_loader import load_to_mysql

# --------------------------------------------------------
# Step 2 : Download NLTK Resources (First Run Only)
# --------------------------------------------------------

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# --------------------------------------------------------
# Step 3 : Read Reviews Dataset
# --------------------------------------------------------

reviews_df = pd.read_csv("data/reviews.csv")

print("=" * 60)
print("REVIEWS DATASET LOADED")
print("=" * 60)
print(reviews_df)

# --------------------------------------------------------
# Step 4 : Convert Text to Lowercase
# --------------------------------------------------------

reviews_df["lowercase"] = reviews_df["review"].str.lower()

print("\nLowercase Conversion")
print(reviews_df[["review", "lowercase"]])

# --------------------------------------------------------
# Step 5 : Remove Punctuation
# --------------------------------------------------------

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

reviews_df["no_punctuation"] = reviews_df["lowercase"].apply(remove_punctuation)

print("\nPunctuation Removed")
print(reviews_df[["lowercase", "no_punctuation"]])

# --------------------------------------------------------
# Step 6 : Remove Numbers
# --------------------------------------------------------

def remove_numbers(text):
    return re.sub(r"\d+", "", text)

reviews_df["no_numbers"] = reviews_df["no_punctuation"].apply(remove_numbers)

print("\nNumbers Removed")
print(reviews_df[["no_punctuation", "no_numbers"]])

# --------------------------------------------------------
# Step 7 : Tokenization
# --------------------------------------------------------

reviews_df["tokens"] = reviews_df["no_numbers"].apply(word_tokenize)

print("\nTokenization")
print(reviews_df[["review", "tokens"]])

# --------------------------------------------------------
# Step 8 : Remove Stop Words
# --------------------------------------------------------

stop_words = set(stopwords.words("english"))

def remove_stopwords(tokens):
    return [word for word in tokens if word not in stop_words]

reviews_df["stopwords_removed"] = reviews_df["tokens"].apply(remove_stopwords)

print("\nStop Words Removed")
print(reviews_df[["tokens", "stopwords_removed"]])

# --------------------------------------------------------
# Step 9 : Stemming
# --------------------------------------------------------

stemmer = PorterStemmer()

def stem_words(tokens):
    return [stemmer.stem(word) for word in tokens]

reviews_df["stemmed"] = reviews_df["stopwords_removed"].apply(stem_words)

print("\nStemming Result")
print(reviews_df[["stopwords_removed", "stemmed"]])

# --------------------------------------------------------
# Step 10 : Lemmatization
# --------------------------------------------------------

lemmatizer = WordNetLemmatizer()

def lemmatize_words(tokens):
    return [lemmatizer.lemmatize(word) for word in tokens]

reviews_df["lemmatized"] = reviews_df["stopwords_removed"].apply(lemmatize_words)

print("\nLemmatization Result")
print(reviews_df[["stopwords_removed", "lemmatized"]])

# --------------------------------------------------------
# Step 11 : Create Final Clean Text
# --------------------------------------------------------

reviews_df["clean_text"] = reviews_df["lemmatized"].apply(
    lambda words: " ".join(words)
)

print("\nFinal Clean Text")
print(reviews_df[["review", "clean_text"]])

# --------------------------------------------------------
# Step 12 : Save Processed Reviews
# --------------------------------------------------------

output_path = "output/processed_reviews.csv"

reviews_df.to_csv(output_path, index=False)

print("\nProcessed reviews saved successfully!")
print(f"Location : {output_path}")

# --------------------------------------------------------
# Step 13 : Load into MySQL
# --------------------------------------------------------

load_to_mysql(reviews_df, "processed_reviews")

print("\nText Processing Pipeline Completed Successfully!")