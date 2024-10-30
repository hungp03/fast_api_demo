from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from core.dbconfig import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    image_path = Column(String(255), nullable=False)
    processed_image_path = Column(String(255), nullable=True)
    resolution = Column(String(50), nullable=True)
    uploaded_at = Column(DateTime, default=datetime.now(timezone.utc))
    edited_at = Column(DateTime, nullable=True)
    status = Column(String(50), default="uploaded")

    user = relationship("User", back_populates="images")
    processing_jobs = relationship("ProcessingJob", back_populates="image")
