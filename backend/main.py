from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
# from routers import task
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Include routes
# app.include_router(task.router, prefix="/api")

# Enable CORS for development
if os.getenv("ENV") != "production":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Vite dev server
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
# Serve frontend
# if os.getenv("ENV") == "production" and os.path.exists("../frontend/dist"):
#     app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="static")