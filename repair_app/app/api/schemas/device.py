from pydantic import BaseModel
from datetime import date
from typing import Optional

class DeviceBase(BaseModel):
    name: str

class DeviceCreate(DeviceBase):
    user_id: int

class DeviceUpdate(DeviceBase):
    name: Optional[str] = None

class Device(DeviceBase):
    id: int
    date_added: date
    user_id: int

    class Config:
        orm_mode = True