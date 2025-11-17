# TODO:
#   Learn about environment variables and how to use a .env file.
#  Create a file named settings.py (for example) and import your environment variables there.
#    You’ll then be able to access them anywhere in your project.
#  Implement a function that accepts an argument and, based on that argument,
#    extracts data from an API.
#  The timestamp should be generated dynamically instead of being static.

import requests
from datetime import date
from pydantic import ValidationError

from settings import *
import pandas as pd

from validate import Validate

df = None


def extract(value):
    global df

    url = URL.format(value, API_KEY)
    r = requests.get(url)

    data = r.json()
    time_series = data['Time Series (Daily)']

    validated_row = []

    for date_key, row in time_series.items():
        try:
            validate = Validate(date=date_key, **row)
            validated_row.append(validate.model_dump())
        except ValidationError as e:
            print(e)

    validated_df = pd.DataFrame(validated_row)

    # validated_data = Validation(data)
    if df is None:
        df = pd.DataFrame.from_dict(time_series, orient='index')  # for the first time add
    else:
        df = pd.concat([df, data], ignore_index=True)  # after just add other dataframes

    ct = date.today()
    df.to_csv(f"extracted_data/{value}_{ct}.csv")
    # print(df)

    return df
