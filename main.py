import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "hello"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )
