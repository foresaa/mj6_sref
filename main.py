from fastapi import FastAPI
from app.api.v1 import endpoints
from app.db.base import Base
from app.db.session import engine
import jwt
from dotenv import load_dotenv
import os
from fastapi.staticfiles import StaticFiles

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# Example for encoding a token
token = jwt.encode({"some": "payload"}, SECRET_KEY, algorithm="HS256")

# Example for decoding a token
decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

# Initialize FastAPI app
app = FastAPI()

# Include API routes from the endpoints module
app.include_router(endpoints.router)

# Mount the /images directory
app.mount("/images", StaticFiles(directory="uploads"), name="images")

# Create database tables
Base.metadata.create_all(bind=engine)
