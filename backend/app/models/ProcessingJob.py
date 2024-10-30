from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from core.dbconfig import Base

class ProcessingJob(Base):
    __tablename__ = "processing_jobs"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    type = Column(String(50), nullable=False)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    completed_at = Column(DateTime, nullable=True)

    # Quan hệ với bảng Image
    image = relationship("Image", back_populates="processing_jobs")
