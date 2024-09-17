from pydantic import BaseModel

class ImageParameterBase(BaseModel):
    file_name: str
    sref_number: int
    sref_description: str
    twitter_id: str

class ImageParameterCreate(ImageParameterBase):
    pass

class ImageParameterResponse(ImageParameterBase):
    id: int

    class Config:
        orm_mode = True
