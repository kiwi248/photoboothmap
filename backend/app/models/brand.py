from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.db.base import Base


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    color_hex = Column(String(7), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
