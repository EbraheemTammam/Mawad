from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import uvicorn
import threading
import webview

from database import Db
from attendance.router import attendance_router

app = FastAPI()
app.include_router(attendance_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    Db.init_db()

def start_fastapi():
    # Run FastAPI in a separate thread
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

def start_webview():
    # Create a webview window
    window = webview.create_window("WorkDay Tracker", "http://127.0.0.1:8000", width=800, height=600)
    webview.start()

if __name__ == "__main__":
    # Start FastAPI in a thread
    fastapi_thread = threading.Thread(target=start_fastapi, daemon=True)
    fastapi_thread.start()

    # Start PyWebView
    start_webview()
