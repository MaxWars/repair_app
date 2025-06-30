from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.api.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=True)
    position = Column(String)
    phone_number = Column(String)

    device = relationship('Device', back_populates='user', uselist=False)
