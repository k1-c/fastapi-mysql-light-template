from fastapi import FastAPI
from service import TTTService


app = FastAPI(
    title="Japan Algo Stock Dev",
    version="1.0.0"
)

@app.get("/")
async def get_internal_wallets():
    return {"hello": "world!"}
