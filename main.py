#TODO:
# Import you created classes there and build your flow inside the main function.

from etl import ETL

obj = ETL()
obj._extract_from_api("AAPL")
obj._extract_from_api("GOOG")

obj._transform()

# obj._load()