from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_users, create_user
from internal.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Usuários"])

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)