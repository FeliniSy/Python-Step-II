from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
# CONN = psycopg2.connect(os.getenv('DATABASE_URL'))

URL = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={0}&apikey=={1}"
