from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, index=True)
    file_path = Column(String)

    def __repr__(self):
        return f"<Image(id={self.id}, file_name={self.file_name})>"

