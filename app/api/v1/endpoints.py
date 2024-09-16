from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.services import user_service, image_service
from app.schemas.image_parameter import ImageParameterCreate
from app.schemas.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/upload/")
async def upload_image(
    parameter: str = Form(...),
    description: str = Form(...),
    x_id: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(user_service.get_current_user)
):
    # Call service layer for image handling
    image_data = ImageParameterCreate(parameter=parameter, description=description, x_id=x_id)
    return image_service.upload_image(image_data, file, db, user)
