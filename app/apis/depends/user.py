from typing import Annotated
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database.helper import get_session
from app.core models.