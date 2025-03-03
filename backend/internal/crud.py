from sqlalchemy.orm import Session
from internal.models.db_models import User, Material, Tracking, Failure
from internal.schemas import UserCreate, MaterialCreate, TrackingCreate, FailureCreate

# CRUD para Usuários
def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# CRUD para Materiais
def get_materials(db: Session):
    return db.query(Material).all()

def create_material(db: Session, material: MaterialCreate):
    db_material = Material(name=material.name, type=material.type, expiration_date=material.expiration_date, serial=material.serial)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

# CRUD para Rastreamento
def get_tracking(db: Session):
    return db.query(Tracking).all()

def create_tracking(db: Session, tracking: TrackingCreate):
    db_tracking = Tracking(material_id=tracking.material_id, stage=tracking.stage, status=tracking.status)
    db.add(db_tracking)
    db.commit()
    db.refresh(db_tracking)
    return db_tracking

# CRUD para Falhas
def get_failures(db: Session):
    return db.query(Failure).all()

def create_failure(db: Session, failure: FailureCreate):
    db_failure = Failure(tracking_id=failure.tracking_id, reason=failure.reason)
    db.add(db_failure)
    db.commit()
    db.refresh(db_failure)
    return db_failure