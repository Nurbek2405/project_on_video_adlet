from sqlalchemy.orm import Session

from app.core.models.user import User


class UserCreateExeption(Exception):
    """ raise exepction when there is an error during user creation"""


class UserRepo:
    def __init__(self, session) -> None:
        self.session = session

    def create(self, instance: User) -> User:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except Exception as e:
            self.session.rollback()
            raise UserCreateExeption(str(e))