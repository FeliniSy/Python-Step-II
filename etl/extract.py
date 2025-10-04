import requests
import json

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=ninis_APIKEY'
r = requests.get(url)
data = r.json()

# print(data)

with open("raw_data\AAPL_2025_10-04.json", "w") as f:
    json.dump(data, f, indent=4)

