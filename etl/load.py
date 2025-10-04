import pandas as pd
import pyodbc
import os
from datetime import datetime
server = 'FELINISY'
database = 'Daily_Stocks'
driver = '{ODBC Driver 17 for SQL Server}'

input_folder = "new_column_data"
filenames = ['AAPL_2025-10-04_cleaned.tsv', 'GOOG_2025-10-04_cleaned.tsv', 'MSFT_2025-10-04_cleaned.tsv']

conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)
cursor = conn.cursor()

cursor.execute('''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='stock_daily_data' AND xtype='U')
BEGIN
    CREATE TABLE stock_daily_data (
        id INT IDENTITY(1,1) PRIMARY KEY,
        symbol NVARCHAR(10),
        date DATE,
        open_price FLOAT,
        high_price FLOAT,
        low_price FLOAT,
        close_price FLOAT,
        volume BIGINT,
        daily_change_percentage FLOAT,
        extraction_timestamp DATETIME DEFAULT GETDATE(),
        CONSTRAINT UQ_stock_date UNIQUE(symbol, date)
    )
END
''')
conn.commit()

for file in filenames:
    input_path = os.path.join(input_folder, file)

    df = pd.read_csv(input_path, sep='\t')

    symbol = file.split('_')[0]
    df['symbol'] = symbol

    for index, row in df.iterrows():
        try:
            cursor.execute('''
                INSERT INTO stock_daily_data 
                (symbol, date, open_price, high_price, low_price, close_price, volume, daily_change_percentage)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', row['symbol'], row['date'], row['open'], row['high'], row['low'], row['close'],
                 row['volume'], row['daily_change_percentage'])
        except pyodbc.IntegrityError:
            pass

    conn.commit()
    print(f"Inserted data from {file}")


# df_sql = pd.read_sql("SELECT * FROM stock_daily_data", conn)
# df_sql.to_json("raw_data/stock_daily_data_export.json", orient="records", indent=4, date_format='iso')

conn.close()