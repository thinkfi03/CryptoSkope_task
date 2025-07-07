import pandas as pd
import requests

def aggregate_data():
    # Dummy aggregation: mean of sample prices
    data = pd.DataFrame({"price": [100, 200, 300, 400, 500]})
    mean_price = data["price"].mean()
    return {"mean_price": mean_price}

def scrape_data(url: str):
    # Simple scraping: get page length
    try:
        r = requests.get(url, timeout=5)
        return {"url": url, "length": len(r.text)}
    except Exception as e:
        return {"error": str(e)}