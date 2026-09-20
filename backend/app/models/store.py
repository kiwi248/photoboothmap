from geoalchemy2 import Geometry
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False, index=True)
    name = Column(String(200), nullable=False)
    address = Column(String(300), nullable=False)
    location = Column(Geometry("POINT", srid=4326), nullable=False)
    phone = Column(String(30))
    is_active = Column(Boolean, nullable=False, default=True)
    last_verified_at = Column(DateTime(timezone=True))
    source_url = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    brand = relationship("Brand")
