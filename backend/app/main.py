from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from routers import api_router

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:3030",
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

# Incluir todas as rotas da API
app.include_router(api_router)

@app.get("/")
def home():
    return {"message": "API do sistema CME está rodando!"}