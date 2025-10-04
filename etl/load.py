import pandas as pd
import pyodbc
import json

with open('raw_data/AAPL_with_new_column.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['symbol'] = 'AAPL'

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=FELINISY;'
    'DATABASE=AAPL_2025;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

for index, row in df.iterrows():
        cursor.execute('''
        IF NOT EXISTS (
            SELECT 1 FROM stock_daily_data
            WHERE symbol = ? AND date = ?
        )
        BEGIN
            INSERT INTO stock_daily_data
            (symbol, date, open_price, high_price, low_price, close_price, volume, daily_change_percentage)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        END
    ''', row['symbol'], row['date'], row['symbol'], row['date'], row['open'], row['high'], 
    row['low'], row['close'], row['volume'], row['daily_change_percentage'])

query  = "select * from stock_daily_data"

df = pd.read_sql(query, conn)

df.to_json("raw_data\stock_daily_data_export.json", orient="records", indent=4, date_format='iso')

conn.commit()
conn.close()


