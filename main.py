from fastapi import FastAPI
from app.api.v1 import endpoints
from app.db.base import Base
from app.db.session import engine

# Initialize FastAPI app
app = FastAPI()

# Include API routes from the endpoints module
app.include_router(endpoints.router)

# Create database tables
Base.metadata.create_all(bind=engine)
