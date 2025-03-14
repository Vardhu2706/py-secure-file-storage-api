# File Model

# Imports
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base

class File(Base):
    __tablename__ = "files"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    original_name = Column(String, nullable=False)
    encrypted_name = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    upload_time = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    user = relationship("User", back_populates="files")