# CryptoSkope

CryptoSkope is a Next.js + TypeScript frontend for cryptocurrency data and dashboards. The project includes a plan to integrate a Python microservice (FastAPI) to handle heavier tasks such as ML predictions, data processing/scraping, blockchain interactions, and specialized risk calculations.

This README explains project structure, how to run the frontend, and how to add/run the Python service and integrate it with the Next.js app.

## Table of contents
- Project overview
- Prerequisites
- Frontend: install & run
- Python service: scaffold & run
- Test Task
- Next.js integration example

## Project overview
- Frontend: Next.js (app router) + React + TypeScript. Main app folder: `app/`.
- Components: reusable UI in `components/`.
- Config constants in `config/constants.ts`.
- Intended Python microservice responsibilities:
  - ML predictions (price forecasting)
  - Data processing & aggregation
  - Web scraping
  - Blockchain interactions (via Web3)
  - Risk analysis calculations

## Prerequisites
- Node.js v22.14.0 
- Python 3.10+ 
- pip
- Windows commands shown below; Linux/macOS similar with `source` for venv

## Frontend: install & run
Open PowerShell or CMD in project root:
```powershell
npm install
npm run dev
# Open http://localhost:3000
```

## Python service: scaffold & run

Example quick scaffold (Windows):
```powershell
cd path\to\CryptoSkope
cd python_service
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn pandas requests web3 scikit-learn
```

- Run locally:
```powershell
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Test Task:
Complete the following API endpoint

- POST /predict        — { "symbol": "BTC" } -> { predicted_price }
- GET /aggregate       — returns aggregated metrics
- POST /scrape         — { "url": "https://..." } -> page info
- POST /blockchain/balance — { "address": "0x..." } -> balance
- POST /risk           — { "symbol": "...", "data": [..] } -> risk_score

## Next.js integration example
Add a small service in `lib/services/pythonService.ts` (or call directly from components/test.tsx):

```typescript
// example: lib/services/pythonService.ts
import axios from "axios";

const BASE = process.env.NEXT_PUBLIC_PYTHON_URL || "http://127.0.0.1:8000";

export async function getPrediction(symbol: string) {
  const { data } = await axios.post(`${BASE}/predict`, { symbol });
  return data;
}
```

