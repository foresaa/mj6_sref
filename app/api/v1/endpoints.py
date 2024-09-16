from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.image import  Image  # Rename import as Image
from app.schemas.image import ImageCreate, ImageResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os

router = APIRouter()

# Path to save uploaded files
UPLOAD_DIRECTORY = "./images/"

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# GET all images
@router.get("/images", response_model=list[ImageResponse])
def get_all_images(db: Session = Depends(get_db)):
    images = db.query(Image).all()
    return images

# POST an image
@router.post("/images", response_model=ImageResponse, status_code=status.HTTP_201_CREATED)
def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    # Save file to the file system
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create a new image record in the database
    image = Image(file_name=file.filename, file_path=file_location)
    db.add(image)
    db.commit()
    db.refresh(image)

    # Return the image response including the file URL
    file_url = f"/images/{file.filename}"
    return {"id": image.id, "file_name": image.file_name, "file_url": file_url}

# DELETE an image by ID
@router.delete("/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")

    # Remove the image file from the file system
    if os.path.exists(image.file_path):
        os.remove(image.file_path)

    # Remove the image record from the database
    db.delete(image)
    db.commit()
    return {"message": "Image deleted successfully"}
