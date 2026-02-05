from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from backend.core.database import Base


class Publication(Base):
    __tablename__ = "publications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    code = Column(String, unique=True, index=True, nullable=False)

    inventory = relationship("Inventory", uselist=False,
                             back_populates="publication", cascade="all, delete-orphan")
    movements = relationship(
        "Movement", back_populates="publication", cascade="all, delete-orphan")
    inventory_history = relationship(
        "InventoryHistory", back_populates="publication", cascade="all, delete-orphan")
