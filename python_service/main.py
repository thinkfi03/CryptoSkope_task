from fastapi import FastAPI
from pydantic import BaseModel
from ml_model import predict_price
from data_processing import aggregate_data, scrape_data
from blockchain import get_balance
from risk_analysis import calculate_risk

app = FastAPI()

class SymbolRequest(BaseModel):
    symbol: str

class DataRequest(BaseModel):
    url: str

class BlockchainRequest(BaseModel):
    address: str

class RiskRequest(BaseModel):
    symbol: str
    data: list

@app.post("/predict")
def predict(req: SymbolRequest):
    return predict_price(req.symbol)

@app.get("/aggregate")
def aggregate():
    return aggregate_data()

@app.post("/scrape")
def scrape(req: DataRequest):
    return scrape_data(req.url)

@app.post("/blockchain/balance")
def balance(req: BlockchainRequest):
    return get_balance(req.address)

@app.post("/risk")
def risk(req: RiskRequest):
    return calculate_risk(req.symbol, req.data)