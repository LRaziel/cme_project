from sqlalchemy import Column, Integer, String, Date, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    expiration_date = Column(Date, nullable=False)
    serial = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials.id"))
    stage = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

class Failure(Base):
    __tablename__ = "failures"

    id = Column(Integer, primary_key=True, index=True)
    tracking_id = Column(Integer, ForeignKey("tracking.id"))
    reason = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
