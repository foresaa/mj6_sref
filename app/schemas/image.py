<<<<<<< HEAD
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class ImageCreate(BaseModel):
    parameter: str
    description: str
    x_id: str

class ImageResponse(BaseModel):
    id: int
    parameter: str
    description: str
    x_id: str
    file_url: str

    class Config:
        orm_mode = True


=======
from pydantic import BaseModel

class ImageCreate(BaseModel):
    parameter: str
    description: str
    x_id: str

class ImageResponse(BaseModel):
    id: int
    parameter: str
    description: str
    x_id: str
    file_url: str

    class Config:
        orm_mode = True
>>>>>>> 31360ec005fc4f95e882871513d4899309140528
