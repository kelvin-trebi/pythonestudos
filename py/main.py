from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def raiz():
    return {"mensagem": "API PicPay Simplificado - FastAPI"} 