import enum

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class FrameCategory(str, enum.Enum):
    SEASONAL = "seasonal"
    COLLAB = "collab"
    BASIC = "basic"
    ANNIVERSARY = "anniversary"


class Frame(Base):
    __tablename__ = "frames"

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=True, index=True)
    title = Column(String(200), nullable=False)
    thumbnail_url = Column(String(500), nullable=False)
    category = Column(Enum(FrameCategory, name="frame_category"), nullable=False)
    tags = Column(ARRAY(String))
    is_active = Column(Boolean, nullable=False, default=True)
    first_seen_at = Column(DateTime(timezone=True), server_default=func.now())

    brand = relationship("Brand")
    store = relationship("Store")
