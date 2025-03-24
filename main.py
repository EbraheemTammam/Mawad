from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import logging

from database import Db
from attendance.router import attendance_router

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(attendance_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    Db.init_db()
