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
