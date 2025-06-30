from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid


from app.api.models import request as request_model
from app.api.schemas import request as request_schema
from app.api.database import get_db

router = APIRouter()


def generate_request_number():
    return str(uuid.uuid4())

@router.post("/requests/", response_model=request_schema.Request)
def create_request(request: request_schema.RequestCreate, db: Session = Depends(get_db)):
    request_number = generate_request_number()
    db_request = request_model.Request(request_number=request_number, **request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

@router.get("/requests/", response_model=List[request_schema.Request])
def read_requests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    requests = db.query(request_model.Request).offset(skip).limit(limit).all()
    return requests

@router.get("/requests/{request_id}", response_model=request_schema.Request)
def read_request(request_id: int, db: Session = Depends(get_db)):
    db_request = db.query(request_model.Request).filter(request_model.Request.id == request_id).first()
    if db_request is None:
        raise HTTPException(status_code=404, detail="Request not found")
    return db_request

@router.put("/requests/{request_id}", response_model=request_schema.Request)
def update_request(request_id: int, request: request_schema.RequestUpdate, db: Session = Depends(get_db)):
    db_request = db.query(request_model.Request).filter(request_model.Request.id == request_id).first()
    if db_request is None:
        raise HTTPException(status_code=404, detail="Request not found")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(db_request, key, value)

    db.commit()
    db.refresh(db_request)
    return db_request

@router.delete("/requests/{request_id}", response_model=request_schema.Request)
def delete_request(request_id: int, db: Session = Depends(get_db)):
    db_request = db.query(request_model.Request).filter(request_model.Request.id == request_id).first()
    if db_request is None:
        raise HTTPException(status_code=404, detail="Request not found")

    db.delete(db_request)
    db.commit()
    return db_request