from fastapi import FastAPI
from backend.config import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API do sistema CME está rodando!"}
