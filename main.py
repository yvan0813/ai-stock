from fastapi import FastAPI
import akshare as ak

app = FastAPI()

@app.get("/analyze/{code}")
def analyze(code: str):
    df = ak.stock_zh_a_hist(symbol=code)
    close = df['收盘'].iloc[-1]
    return {"code": code, "price": close}
