import pandas as pd
import json
import os

input_folder = "extracted_data"
output_folder = "new_column_data"
os.makedirs(output_folder, exist_ok=True)

filenames = ['AAPL_2025-10-04.json', 'GOOG_2025-10-04.json', 'MSFT_2025-10-04.json']

for file in filenames:
    input_path = os.path.join(input_folder, file)
    
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