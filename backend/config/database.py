import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

SQLALCHEMY_DATABASE_URL = "postgresql://cme_user:cme_password@db/cme_db"

# Tenta conectar ao banco de dados com várias tentativas
for attempt in range(10):
  try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    connection = engine.connect()
    print(f"Conectado ao banco de dados na tentativa {attempt + 1}!")
    connection.close()
    break
  except psycopg2.OperationalError:
    print(f"Banco de dados não está pronto, tentativa {attempt + 1}/10...")
    time.sleep(5)
else:
  print("Falha ao conectar ao banco de dados após 10 tentativas!")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Obtém uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()