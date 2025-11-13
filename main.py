#TODO:
# Import you created classes there and build your flow inside the main function.
from etl import ETL

ETL.extract_from_api("AAPL")
ETL.extract_from_api("GOOG")

ETL.transform()

ETL.load()