from app.services.image_service import save_file
from fastapi import APIRouter, Depends, Form, HTTPException, status, File, UploadFile, Request
from sqlalchemy.orm import Session
from app.schemas.image import ImageCreate, ImageResponse
from app.models.image_parameter import ImageParameter
from fastapi.staticfiles import StaticFiles
import shutil
import os

# Initialize the router
router = APIRouter()

try:
    from app.db.session import get_db
except ImportError:
    # Mock function for documentation generation
    def get_db():
        pass

# Image upload directory
UPLOAD_DIR = "uploads/"

@router.post("/images", response_model=ImageResponse, status_code=status.HTTP_201_CREATED)
async def create_image(
    sref_number: int = Form(...),
    sref_description: str = Form(...),
    twitter_id: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Endpoint to upload an image with additional parameters
    """
    try:
        # Save the uploaded file
        file_path = save_file(file, UPLOAD_DIR)
        
        # Create a new Image record
        image = ImageParameter(
            file_name=file.filename,
            file_path=file_path,
            sref_number=sref_number,
            sref_description=sref_description,
            twitter_id=twitter_id
        )
        db.add(image)
        db.commit()
        db.refresh(image)
        
        # Prepare the file URL and other response fields
        file_url = f"{UPLOAD_DIR}{file.filename}"
        
        return {
            "id": image.id,
            "file_name": image.file_name,
            "file_url": file_url,
            "x_id": sref_number,  # Add appropriate values here if needed
            "description": sref_description,
            "parameter": "N/A"  # Replace with actual parameter if needed
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Retrieve all images (GET request)
@router.get("/images", response_model=list[ImageResponse])
async def get_all_images(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all uploaded images
    """
    images = db.query(ImageParameter).all()
    
    if not images:
        raise HTTPException(status_code=404, detail="No images found")
    
    image_responses = []
    for image in images:
        file_url = f"{UPLOAD_DIR}{image.file_name}"
        image_responses.append({
            "id": image.id,
            "file_name": image.file_name,
            "file_url": file_url,
            "x_id": image.sref_number,
            "description": image.sref_description,
            "parameter": "N/A"  # Replace with actual parameter if needed
        })
    
    return image_responses

# Delete an image by ID
@router.delete("/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_image(image_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete an image by ID
    """
    image = db.query(ImageParameter).filter(ImageParameter.id == image_id).first()
    
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # Delete the image file from the server
    os.remove(image.file_path)
    
    # Delete the image record from the database
    db.delete(image)
    db.commit()

    return {"message": "Image deleted successfully"}

# Serve static files
router.mount("/static", StaticFiles(directory="static"), name="static")
