from fastapi import FastAPI
from config.database import Base, engine
from routers import api_router

app = FastAPI()

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

# Incluir todas as rotas da API
app.include_router(api_router)

@app.get("/")
def home():
    return {"message": "API do sistema CME está rodando!"}
