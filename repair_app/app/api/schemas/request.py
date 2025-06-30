from pydantic import BaseModel
from typing import Optional

class RequestBase(BaseModel):
    request_number: str
    description: Optional[str] = None

class RequestCreate(RequestBase):
    device_id: int

class RequestUpdate(RequestBase):
    request_number: Optional[str] = None
    description: Optional[str] = None

class Request(RequestBase):
    id: int
    device_id: int

    class Config:
        orm_mode = True