from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    full_name: str
    position: Optional[str] = None
    phone_number: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    full_name: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True