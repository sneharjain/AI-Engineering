import pandas as pd
from sqlalchemy import create_engine

# ---------- Extract ----------
df = pd.read_csv("data/student.csv")

# ---------- Transform ----------
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].mean())

# ---------- Load ----------
engine = create_engine(
    "mysql+pymysql://root:AiBootcamp%402026@localhost:3307/ai_engineering_db"
)

df.to_sql(
    name="clean_students",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data cleaned and loaded into MySQL.")