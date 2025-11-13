import requests
from pathlib import Path
import json
from settings import API_KEY
from datetime import date

class Names:
    def __init__(self,name):
        self.name=name

    def extract_from_api(self):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.name}&apikey=={API_KEY}"
        r = requests.get(url)
        data = r.json()

        ct = date.today()

        file_path = Path("updated_extracted_data") / f"{self.name}_{ct}.json"

        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open("w") as f1:
            json.dump(data, f1, indent=4)

