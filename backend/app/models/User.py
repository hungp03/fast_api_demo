from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime, timezone
from core.dbconfig import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)

    images = relationship("Image", back_populates="user")
