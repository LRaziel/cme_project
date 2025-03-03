from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_tracking, create_tracking
from internal.schemas import TrackingCreate, TrackingResponse

router = APIRouter(prefix="/tracking", tags=["Rastreamento"])

@router.get("/", response_model=list[TrackingResponse])
def list_tracking(db: Session = Depends(get_db)):
    return get_tracking(db)

@router.post("/", response_model=TrackingResponse)
def create_tracking(tracking: TrackingCreate, db: Session = Depends(get_db)):
    return create_tracking(db, tracking)