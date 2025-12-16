from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.core.database import Base 

class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    publication_id = Column(Integer, ForeignKey("publications.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    movement_type = Column(String, nullable=False)  # e.g., 'in' or 'out'
    timestamp = Column(String, nullable=False, default=datetime.utcnow().isoformat())
    notes = Column(String, nullable=True)

    user = relationship("User", back_populates="movements")
    publication = relationship("Publication", back_populates="movements")
    