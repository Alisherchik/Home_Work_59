import sqlite3
import pandas as pd
import random
# pip install pandas
# pip install openpyxl
def convert_to_excel(table):
    connection = sqlite3.connect("data2.db")
    df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 10;", connection)
    connection.close()
    name = f"base_{random.randint(1,10000000000)}_{table}.xlsx"
    df.to_excel(name, index=False)
    return name
convert_to_excel("user")