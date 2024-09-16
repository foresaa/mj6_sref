from pydantic import BaseModel

class ImageParameterCreate(BaseModel):
    parameter: str
    description: str
    x_id: str
