from pydantic import BaseModel
from datetime import date

# Schema para criação de usuário
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

# Schema para resposta de usuário (sem senha)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True

# Schema para criação de material
class MaterialCreate(BaseModel):
    name: str
    type: str
    expiration_date: date

# Schema para resposta de material
class MaterialResponse(MaterialCreate):
    id: int
    serial: str
    stage:str
    status: str

    class Config:
        from_attributes = True

# Schema para criação de rastreamento
class TrackingCreate(BaseModel):
    material_id: int
    stage: str
    status: str

# Schema para resposta de rastreamento
class TrackingResponse(TrackingCreate):
    id: int

    class Config:
        from_attributes = True

# Schema para criação de falha
class FailureCreate(BaseModel):
    tracking_id: int
    reason: str

# Schema para resposta de falha
class FailureResponse(FailureCreate):
    id: int

    class Config:
        from_attributes = True