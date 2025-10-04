from pydantic import BaseModel, ValidationError

class StockData(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    daily_change_percentage: float

raw_data = [
    {"date": "2025-10-03", "open": 184.23, "high": 185.44, "low": 182.61,
     "close": 183.45, "volume": 55432123, "daily_change_percentage": -0.42},
    {"date": "2025-10-02", "open": "wrong_value", "high": 186.50, "low": 184.00,
     "close": 185.10, "volume": 43219876, "daily_change_percentage": -0.48}
]

for record in raw_data:
    try:
        validated = StockData(**record)
        print("Valid:", validated)
    except ValidationError as e:
        print("Invalid record:", e)
