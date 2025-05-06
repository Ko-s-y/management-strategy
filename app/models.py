from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class UnitType(enum.Enum):
    GRAM = "g"
    MILLILITER = "ml"
    BOTTLE = "bottle"
    PIECE = "piece"
    BOX = "box"
    PACK = "pack"

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    unit_type = Column(Enum(UnitType), nullable=False)
    unit_value = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
