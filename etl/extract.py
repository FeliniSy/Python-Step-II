import requests
import json
from settings import API_KEY

# TODO:
#   Learn about environment variables and how to use a .env file.
#  Create a file named settings.py (for example) and import your environment variables there.
#    You’ll then be able to access them anywhere in your project.
#  Implement a function that accepts an argument and, based on that argument,
#    extracts data from an API.
#  The timestamp should be generated dynamically instead of being static.

APIKEY=API_KEY

# data for MSFT
url1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey==APIKEY'
r1 = requests.get(url1)
data1 = r1.json()

# print(data)

with open("extracted_data\MSFT_2025-10-04.json", "w") as f1:
    json.dump(data1, f1, indent=4)

# data for GOOG
url2 = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOG&apikey==APIKEY'
r2 = requests.get(url2)
data2 = r2.json()

# print(data)

with open("extracted_data\GOOG_2025-10-04.json", "w") as f2:
    json.dump(data2, f2, indent=4)


# data for AAPL
url3 = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey==APIKEY'
r3 = requests.get(url3)
data3 = r3.json()

# print(data)

with open("extracted_data\AAPL_2025-10-04.json", "w") as f3:
    json.dump(data3, f3, indent=4)
