""" app/services/image_service.py """

def upload_image(image_data, file, db, user):
    # Logic for image upload
    return {"message": "Image uploaded successfully"}


""" save_file"""
import os
from fastapi import UploadFile
from pathlib import Path

UPLOAD_DIRECTORY = "uploads/"

def save_file(file: UploadFile, destination_dir: str = UPLOAD_DIRECTORY) -> str:
    # Ensure the upload directory exists
    Path(destination_dir).mkdir(parents=True, exist_ok=True)

    file_path = os.path.join(destination_dir, file.filename)
    
    # Write the file to the specified directory
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    return file_path  # Return the full path of the saved file

