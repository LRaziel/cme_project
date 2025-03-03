from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_materials, create_material
from internal.schemas import MaterialCreate, MaterialResponse

router = APIRouter(prefix="/materials", tags=["Materiais"])

@router.get("/", response_model=list[MaterialResponse])
def list_materials(db: Session = Depends(get_db)):
    return get_materials(db)

@router.post("/", response_model=MaterialResponse)
def create_material(material: MaterialCreate, db: Session = Depends(get_db)):
    return create_material(db, material)