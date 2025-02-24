from app.core.schemas.base import BaseSchema
from typing import Optional

class UserRead(BaseSchema):
    id: int
    username: str
    password: str

    first_name: str
    last_name: str
    middle_name: Optional[str] = None

    is_active: bool
    is_staff: bool
    is_superuser: bool


class UserCreate(BaseSchema):
    username: str
    password: str

    first_name: str
    last_name: str
    middle_name: Optional[str] = None

    is_active: Optional[bool] = True
    is_staff: Optional[bool] = False
    is_superuser: Optional[bool] = False


class UserUpdate(BaseSchema):
    username: Optional[str] = None
    password: Optional[str] = None

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None

    is_active: Optional[bool] = True
    is_staff: Optional[bool] = False
    is_superuser: Optional[bool] = False
