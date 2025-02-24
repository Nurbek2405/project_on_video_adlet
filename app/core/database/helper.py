# помогает подключиться к базе данных

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DB_URL

engine = create_engine(
    url = DB_URL,
    echo=False,
)

Session = sessionmaker(bind=engine)

def get_session():
    with Session() as session:
        yield session