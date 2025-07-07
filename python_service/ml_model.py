import random

def predict_price(symbol: str):
    # Dummy ML model: returns a random price
    price = round(random.uniform(10, 1000), 2)
    return {"symbol": symbol, "predicted_price": price}