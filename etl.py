import pandas as pd
import psycopg2
import requests
from pathlib import Path
import json

from settings import *
from datetime import date

class ETL:

    @staticmethod
    def extract_from_api(name):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={name}&apikey=={API_KEY}"
        r = requests.get(url)
        data = r.json()

        ct = date.today()

        file_path = Path("updated_extracted_data") / f"{name}_{ct}.json"

        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open("w") as f1:
            json.dump(data, f1, indent=4)

    @staticmethod
    def transform():
        input_folder = "updated_extracted_data/"
        output_folder = "updated_newcolumndata/"
        os.makedirs(output_folder, exist_ok=True)

        fileList = os.listdir(input_folder)
        
        for file in fileList:
            input_path = os.path.join(input_folder,file)
            with open(input_path, 'r') as f:
                data = json.load(f)

            time_series = data['Time Series (Daily)']

            df = pd.DataFrame.from_dict(time_series, orient='index')

            df.columns = ['open', 'high', 'low', 'close', 'volume']

            df = df.reset_index().rename(columns={'index': 'date'})

            df['date'] = pd.to_datetime(df['date'])
            df[['open', 'high', 'low', 'close']] = df[['open', 'high', 'low', 'close']].astype(float)
            df['volume'] = df['volume'].astype(int)

            df['daily_change_percentage'] = ((df['close'] - df['open']) / df['open']) * 100

            output_filename = file.replace('.json', '_cleaned.tsv')
            output_path = os.path.join(output_folder, output_filename)
            df.to_csv(output_path, sep='\t', index=False, float_format='%.2f')
            
            print(f"{file} -> {output_path}")

    @staticmethod
    def load():
        input_folder = "updated_newcolumndata/"
        fileList = os.listdir(input_folder)

        conn = psycopg2.connect(CONN)
        cur =  conn.cursor()
        cur.execute('''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='stock_daily_data' AND xtype='U')
        BEGIN
            CREATE TABLE stock_daily_data (
                id INT SERIAL PRIMARY KEY,
                symbol VARCHAR(10),
                date DATE,
                open_price FLOAT,
                high_price FLOAT,
                low_price FLOAT,
                close_price FLOAT,
                volume BIGINT,
                daily_change_percentage FLOAT,
                extraction_timestamp DATETIME DEFAULT NOW(),
                CONSTRAINT UQ_stock_date UNIQUE(symbol, date)
            )
        END
        ''')
        CONN.commit()

        for file in fileList:
            input_path = os.path.join(input_folder,file)
            df = pd.read_csv(input_path,sep='\t')

            symbol = file.split('_')[0]
            df['symbol'] = symbol

            for index, row in df.iterrows():
                try:
                    cur.execute('''
                        INSERT INTO stock_daily_data
                        (symbol, date, open_price, high_price, low_price, close_price, volume, daily_change_percentage)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', row['symbol'], row['date'], row['open'], row['high'], row['low'], row['close'],
                                   row['volume'], row['daily_change_percentage'])
                except psycopg2.IntegrityError:
                    pass

            CONN.commit()
            print(f"Inserted data from {file}")

        CONN.close()