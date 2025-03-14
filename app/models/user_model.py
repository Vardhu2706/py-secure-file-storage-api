# User Model

# Import
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    files = relationship("File", back_populates="user")