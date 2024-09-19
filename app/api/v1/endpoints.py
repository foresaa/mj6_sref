from fastapi import APIRouter, Depends, Form, HTTPException, status, File, UploadFile, Request
from sqlalchemy.orm import Session
#from app.db.session import get_db
from app.schemas.image import ImageCreate, ImageResponse
from app.models.image_parameter import ImageParameter
from fastapi.staticfiles import StaticFiles
import shutil
import os


try:
    from app.db.session import get_db
except ImportError:
    # Mock function for documentation generation
    def get_db():
        pass

router = APIRouter()

UPLOAD_DIRECTORY = "uploads"

# GET all images
@router.get("/images", response_model=list[ImageResponse])
def get_all_images(db: Session = Depends(get_db)):
    images = db.query(ImageParameter).all()
    return images

## POST an image with additional parameters
@router.post("/images", response_model=ImageResponse, status_code=status.HTTP_201_CREATED)
def upload_image(
    request: Request,
    file: UploadFile = File(...),
    sref_number: int = Form(...),
    sref_description: str = Form(...),
    twitter_id: str = Form(...),
    db: Session = Depends(get_db)
):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    # Save file to the file system
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Create a new image record in the database
    image = ImageParameter(
        file_name=file.filename, 
        file_path=file_location, 
        sref_number=sref_number,
        sref_description=sref_description,
        twitter_id=twitter_id
    )
    db.add(image)
    db.commit()
    db.refresh(image)

    # Return the image response including the file URL
    file_url = f"{request.url.scheme}://{request.url.hostname}/images/{file.filename}"
    return {"id": image.id, "file_name": image.file_name, "file_url": file_url}


    # Return the image response including the file URL
    file_url = f"{request.url.scheme}://{request.url.hostname}/images/{file.filename}"
    return {"id": image.id, "file_name": image.file_name, "file_url": file_url}

# DELETE an image by ID
@router.delete("/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(ImageParameter).filter(ImageParameter.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Remove the image file from the file system
    if os.path.exists(image.file_path):
        os.remove(image.file_path)

    # Delete the image from the database
    db.delete(image)
    db.commit()
    return {"message": "Image deleted successfully"}
