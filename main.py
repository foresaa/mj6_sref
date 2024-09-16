from fastapi import FastAPI
from app.api.v1 import endpoints
from app.db.base import Base
from app.db.session import engine

import jwt

# Example for encoding a token
token = jwt.encode({"some": "payload"}, "your-secret-key", algorithm="HS256")

# Example for decoding a token
decoded = jwt.decode(token, "your-secret-key", algorithms=["HS256"])


# Initialize FastAPI app
app = FastAPI()

# Include API routes from the endpoints module
app.include_router(endpoints.router)

# Create database tables
Base.metadata.create_all(bind=engine)
