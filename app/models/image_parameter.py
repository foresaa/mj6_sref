from sqlalchemy import Column, Integer, String
from app.db.base import Base

class ImageParameter(Base):
    __tablename__ = "image_parameters"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    file_path = Column(String)
    sref_number = Column(Integer)
    sref_description = Column(String)
    twitter_id = Column(String)
