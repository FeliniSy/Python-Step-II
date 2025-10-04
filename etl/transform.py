import pandas as pd
import json


# read the json file and organize data into columns``
with open('raw_data/AAPL_2025_10-04.json') as f:
    data = json.load(f)

time_series = data['Time Series (5min)']
df = pd.DataFrame.from_dict(time_series, orient='index')

df.columns = [
    'open', 'high', 'low', 'close', 'volume'
]

df = df.reset_index().rename(columns={'index': 'date'})

df['date'] = pd.to_datetime(df['date'])
df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
df["volume"] = df["volume"].astype(int)

# print(df)

# add the new columns
df['daily_change_percentage'] = (df['close'] - df['open'])/df['open'] * 100
print(df)

# save the transformed data to a new json file
df.to_json('raw_data/AAPL_with_new_column.json', orient='records', indent=4, date_format='iso')