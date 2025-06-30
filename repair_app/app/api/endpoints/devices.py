from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date


from app.api.models import device as device_model
from app.api.schemas import device as device_schema
from app.api.database import get_db

router = APIRouter()

@router.post("/devices/", response_model=device_schema.Device)
def create_device(device: device_schema.DeviceCreate, db: Session = Depends(get_db)):
    db_device = device_model.Device(**device.dict())  # Создаем объект Device из схемы
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

@router.get("/devices/", response_model=List[device_schema.Device])
def read_devices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    devices = db.query(device_model.Device).offset(skip).limit(limit).all()
    return devices

@router.get("/devices/{device_id}", response_model=device_schema.Device)
def read_device(device_id: int, db: Session = Depends(get_db)):
    db_device = db.query(device_model.Device).filter(device_model.Device.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device

@router.put("/devices/{device_id}", response_model=device_schema.Device)
def update_device(device_id: int, device: device_schema.DeviceUpdate, db: Session = Depends(get_db)):
    db_device = db.query(device_model.Device).filter(device_model.Device.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")

    for key, value in device.dict(exclude_unset=True).items():
        setattr(db_device, key, value)  #  Обновляем поля

    db.commit()
    db.refresh(db_device)
    return db_device

@router.delete("/devices/{device_id}", response_model=device_schema.Device)
def delete_device(device_id: int, db: Session = Depends(get_db)):
    db_device = db.query(device_model.Device).filter(device_model.Device.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")

    db.delete(db_device)
    db.commit()
    return db_device