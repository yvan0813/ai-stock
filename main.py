from fastapi import FastAPI
import akshare as ak
import os

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "API is running"}


@app.get("/analyze/{code}")
def analyze(code: str):
    try:
        df = ak.stock_zh_a_hist(symbol=code)
        close = df["收盘"].iloc[-1]

        return {
            "code": code,
            "price": float(close)
        }
    except Exception as e:
        return {
            "error": str(e)
        }


# ✅ 关键：用 Railway 的 PORT
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))  # ← 核心就在这里

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port
    )
