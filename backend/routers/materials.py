from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_materials, get_materials_with_tracking, create_new_material, get_materials_by_stage, get_materials_by_status
from internal.schemas import MaterialCreate, MaterialResponse

router = APIRouter(prefix="/materials", tags=["Materiais"])

@router.get("/", response_model=list[MaterialResponse])
def list_materials(db: Session = Depends(get_db)):
    return get_materials(db)

@router.get("/stage/{stage}", response_model=list[MaterialResponse])
def list_materials_by_stage(stage: str, db: Session = Depends(get_db)):
    materials = get_materials_by_stage(db, stage)
    if not materials:
        raise HTTPException(status_code=404, detail="No materials found in this stage")
    return materials

@router.get("/status/{status}", response_model=list[MaterialResponse])
def list_materials_by_status(status: str, db: Session = Depends(get_db)):
    materials = get_materials_by_status(db, status)
    if not materials:
        raise HTTPException(status_code=404, detail="No materials found with this status")
    return materials

@router.post("/", response_model=MaterialResponse)
def create_material(material: MaterialCreate, db: Session = Depends(get_db)):
    return create_new_material(db, material)

@router.get("/with-tracking", response_model=list[MaterialResponse])
def list_materials_with_tracking(db: Session = Depends(get_db)):
    return get_materials_with_tracking(db)