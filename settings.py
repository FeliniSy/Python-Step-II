import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv('API_KEY')
CONN = psycopg2.connect(os.getenv('DATABASE_URL'))