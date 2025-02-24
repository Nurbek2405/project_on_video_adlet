# помогает подключиться к базе данных

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DB_URL, DB_ECHO

engine = create_engine(   #
    url = DB_URL,
    echo = DB_ECHO, # TRUE чтобы выходило в консоль?
)

SessionLocal = sessionmaker(bind=engine)  # привязаны к мостику

def get_session():       # создаем
    with SessionLocal() as session:    # обращаемся и делаем сессию
        yield session                  # создает сессию, пользуемся сессией в памяти, как закончим, что надо удалять из памяти