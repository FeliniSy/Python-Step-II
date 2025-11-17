#TODO:
# Import you created classes there and build your flow inside the main function.
from etl.extract import extract
from etl.transform import Transform

temp = extract("AAPL")

obj1 = Transform(temp)
obj1.tranform_data()
