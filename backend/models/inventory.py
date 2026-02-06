from sqlalchemy import Integer, DateTime, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.core.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    publication_id = Column(Integer, ForeignKey("publications.id"), nullable=False)
    total_quantity = Column(Integer, nullable=False)
    available_quantity = Column(Integer, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)

    publication = relationship("Publication", back_populates="inventory")
    inventory_history = relationship("InventoryHistory", back_populates="inventory", cascade="all, delete-orphan")


class InventoryHistory(Base):
    __tablename__ = "inventory_history"

    id = Column(Integer, primary_key=True, index=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"), nullable=False)
    total_quantity = Column(Integer, nullable=False)
    available_quantity = Column(Integer, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow)

    inventory = relationship("Inventory", back_populates="inventory_history")
