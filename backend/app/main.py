import logging
from fastapi import FastAPI
from .routes import router
from fastapi.middleware.cors import CORSMiddleware
from logging.handlers import RotatingFileHandler

app = FastAPI()

app.include_router(router, prefix="/api")

debug_handler = RotatingFileHandler("app.log", maxBytes=5*1024*1024, backupCount=5)  # 5MB log file
error_handler = RotatingFileHandler("error.log", maxBytes=5*1024*1024, backupCount=5)

# Set levels for each handler
debug_handler.setLevel(logging.DEBUG)
error_handler.setLevel(logging.ERROR)

# Define a log format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
debug_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Get the logger instance and add handlers
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Global logging level
logger.addHandler(debug_handler)
logger.addHandler(error_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, can be restricted to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers (authorization, content-type, etc.)
)
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB!"}
