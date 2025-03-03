from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_failures, create_failure
from internal.schemas import FailureCreate, FailureResponse

router = APIRouter(prefix="/failures", tags=["Falhas"])

@router.get("/", response_model=list[FailureResponse])
def list_failures(db: Session = Depends(get_db)):
    return get_failures(db)

@router.post("/", response_model=FailureResponse)
def create_failure(failure: FailureCreate, db: Session = Depends(get_db)):
    return create_failure(db, failure)