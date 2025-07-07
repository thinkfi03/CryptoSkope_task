def calculate_risk(symbol: str, data: list):
    # Dummy risk: standard deviation as risk score
    if not data:
        return {"symbol": symbol, "risk_score": 0}
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    risk_score = variance ** 0.5
    return {"symbol": symbol, "risk_score": risk_score}