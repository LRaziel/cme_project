from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_tracking, create_new_tracking, get_tracking_by_serial, get_failures_by_serial, generate_pdf_report, generate_xlsx_report
from internal.schemas import TrackingCreate, TrackingResponse, FailureResponse
from fastapi.responses import FileResponse

router = APIRouter(prefix="/tracking", tags=["Rastreamento"])

@router.get("/", response_model=list[TrackingResponse])
def list_tracking(db: Session = Depends(get_db)):
    return get_tracking(db)

@router.get("/{serial}", response_model=list[TrackingResponse])
def list_tracking_by_serial(serial: str, db: Session = Depends(get_db)):
    tracking = get_tracking_by_serial(db, serial)
    if not tracking:
        raise HTTPException(status_code=404, detail="Tracking not found")
    return tracking

@router.get("/{serial}/failures", response_model=list[FailureResponse])
def list_failures_by_serial(serial: str, db: Session = Depends(get_db)):
    failures = get_failures_by_serial(db, serial)
    if not failures:
        raise HTTPException(status_code=404, detail="Failures not found")
    return failures

@router.post("/", response_model=TrackingResponse)
def create_tracking(tracking: TrackingCreate, db: Session = Depends(get_db)):
    return create_new_tracking(db, tracking)

@router.get("/report/pdf", response_class=FileResponse)
def get_pdf_report(db: Session = Depends(get_db)):
    file_path = generate_pdf_report(db)
    return FileResponse(file_path, media_type='application/pdf', filename='report.pdf')

@router.get("/report/xlsx", response_class=FileResponse)
def get_xlsx_report(db: Session = Depends(get_db)):
    file_path = generate_xlsx_report(db)
    return FileResponse(file_path, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename='report.xlsx')