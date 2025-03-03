from sqlalchemy.orm import Session
from internal.models.db_models import User, Material, Tracking, Failure
from internal.schemas import UserCreate, MaterialCreate, TrackingCreate, FailureCreate
import hashlib

# CRUD para Usuários
def get_users(db: Session):
    return db.query(User).all()

def get_users_by_role(db: Session, role: str):
    return db.query(User).filter(User.role == role).all()

def create_new_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# CRUD para Materiais
def generate_serial(name: str) -> str:
    return hashlib.md5(name.encode()).hexdigest()

def get_materials(db: Session):
    return db.query(Material).all()

def get_materials_by_stage(db: Session, stage: str):
    return db.query(Material).join(Tracking).filter(Tracking.stage == stage).all()

def get_materials_by_status(db: Session, status: str):
    return db.query(Material).join(Tracking).filter(Tracking.status == status).all()

def create_new_material(db: Session, material: MaterialCreate):
    serial = generate_serial(material.name)
    db_material = Material(name=material.name, type=material.type, expiration_date=material.expiration_date, serial=serial)
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