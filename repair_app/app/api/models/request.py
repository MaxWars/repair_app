from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.api.database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    request_number = Column(String, unique=True, nullable=False)
    description = Column(String)
    device_id = Column(Integer, ForeignKey("devices.id"))

    device = relationship("Device", back_populates="request")