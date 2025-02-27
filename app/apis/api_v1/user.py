from fastapi import APIRouter, Depends
from typing import Annotated
from app.core.services.user import UserService
from app.apis.depends.user import get_user_service

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/")
def user_create(service: Annotated[UserService, Depends(get_user_service)]):
    pass

