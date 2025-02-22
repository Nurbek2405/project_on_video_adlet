from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DB_URL

engine = create_engine(
    url=DB_URL,
    echo=True,  # DB ECHO чето не признает
)

SessionLocal = sessionmaker(bind=engine)


def get_session():
    with SessionLocal() as session:
        yield session
