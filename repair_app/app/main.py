from fastapi import FastAPI
from app.api.endpoints import users, devices, requests
from app.api.database import Base, engine

app = FastAPI()

app.include_router(users.router)
app.include_router(devices.router)
app.include_router(requests.router)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)