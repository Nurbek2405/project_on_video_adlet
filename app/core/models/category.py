from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.models.base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    users = relationship("User", secondary="user_categories", back_populates="categories")
