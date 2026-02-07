from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship 
from datetime import datetime 
from backend.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    total_publications = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    

    role = relationship("Role")
    movements = relationship("Movement", back_populates="user", cascade="all, delete-orphan")