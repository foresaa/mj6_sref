from sqlalchemy import Column, Integer, String
from app.db.base import Base

class ImageParameter(Base):
    __tablename__ = "image_parameters"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    file_path = Column(String, index=True)
