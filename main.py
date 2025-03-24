from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import Db
from attendance.router import attendance_router

app = FastAPI()
app.include_router(attendance_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    Db.init_db()
