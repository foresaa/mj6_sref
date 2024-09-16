from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.db.base import Base

class ImageParameter(Base):
    __tablename__ = "image_parameters"

    id = Column(Integer, primary_key=True, index=True)
    parameter = Column(String)
    description = Column(Text)
    x_id = Column(String)
    image_url = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
