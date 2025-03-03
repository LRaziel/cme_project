from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_users, create_user, get_users_by_role
from internal.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Usuários"])

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/role/{role}", response_model=list[UserResponse])
def list_users_by_role(role: str, db: Session = Depends(get_db)):
    users = get_users_by_role(db, role)
    if not users:
        raise HTTPException(status_code=404, detail="No users found with this role")
    return users

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)