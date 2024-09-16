from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List
from pydantic import BaseModel
from fastapi.responses import JSONResponse

router = APIRouter()

# Mock database to hold uploaded parameters for now
db = []

# Model for uploaded data
class UploadData(BaseModel):
    parameter: str
    description: str
    x_id: str
    file_name: str

# POST - Original Upload an image with metadata
@router.post("/upload/")
async def upload_image(
    parameter: str = Form(...),
    description: str = Form(...),
    x_id: str = Form(...),
    file: UploadFile = File(...)
):
    # Simulate storing the file and metadata
    file_data = {
        "parameter": parameter,
        "description": description,
        "x_id": x_id,
        "file_name": file.filename,
    }
    db.append(file_data)

    return {"info": "File uploaded successfully", "file_data": file_data}

# GET - Retrieve all uploaded data
@router.get("/uploads/", response_model=List[UploadData])
async def get_all_uploads():
    if not db:
        raise HTTPException(status_code=404, detail="No uploads found")
    return db

# DELETE - Delete an uploaded item by parameter
@router.delete("/upload/{parameter}")
async def delete_upload(parameter: str):
    global db
    db = [item for item in db if item['parameter'] != parameter]
    return JSONResponse(content={"detail": f"Upload with parameter '{parameter}' deleted"})
