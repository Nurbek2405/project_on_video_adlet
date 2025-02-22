from sqlalchemy.orm import Session
from app.core.models.user import User

class UserCreateExeption(Exception):
    """ raise exeption when there is an error during user creation"""


class UserRepo:
    def __init__(self, session: Session) -> None:
        self.session = session  # чтобы наши запросы отправлялись в базу данных или коммиты

    def create(self, instance: User) -> User:
        try:
            self.session.add(instance)
            self.session.commit()  # коммит, это как добавление в базу данных
            self.session.refresh(instance)
            return instance

        except Exception as e:
            self.session.rollback()
            raise UserCreateExeption(e)