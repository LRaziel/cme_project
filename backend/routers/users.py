from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from internal.crud import get_users, create_new_user, get_users_by_role
from internal.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Usuários"])

# Lista todos os usuários
@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

# Lista usuários por função
@router.get("/role/{role}", response_model=list[UserResponse])
def list_users_by_role(role: str, db: Session = Depends(get_db)):
    users = get_users_by_role(db, role)
    if not users:
        raise HTTPException(status_code=404, detail="No users found with this role")
    return users

# Cria um novo usuário
@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(db, user)