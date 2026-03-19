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


# ✅ 关键：兼容本地 + Railway（不会锁死8080）
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))  # ✅ Railway会注入PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
