"""
Reusable MySQL Loader
Notebook 3 - AI Engineering Bootcamp
"""

import pandas as pd
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:AiBootcamp%402026@localhost:3307/ai_engineering_db"
)

def load_to_mysql(df, table_name):
    """
    Load any DataFrame into MySQL.
    Converts Python lists into comma-separated strings.
    """

    mysql_df = df.copy()

    # Convert list columns into strings
    for column in mysql_df.columns:
        mysql_df[column] = mysql_df[column].apply(
            lambda x: ", ".join(x) if isinstance(x, list) else x
        )

    mysql_df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"'{table_name}' loaded into MySQL successfully!")

def verify_table(table_name):
    """
    Read a table back from MySQL.
    """

    result = pd.read_sql(f"SELECT * FROM {table_name};", engine)
    print(result)

    return result