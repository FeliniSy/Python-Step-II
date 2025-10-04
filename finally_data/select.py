import pandas as pd
import pyodbc

server = 'FELINISY'
database = 'Daily Stocks'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)

query = "SELECT * FROM stock_daily_data"
df = pd.read_sql(query, conn)

conn.close()

df.to_json("finally_data/stock_daily_data_export.json", orient="records", indent=4, date_format='iso')

