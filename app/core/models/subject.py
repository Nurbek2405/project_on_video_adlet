from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.core.models.base import Base

class Subject(Base):
    __tablename__ = 'subjects'

    name: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey=True)
