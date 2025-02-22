from app.core.models.user import User
from app.core.schemas.user import UserCreate
from app.core.repos.user import UserRepo

#api -> services -> repo

class UserService:
    def __init__(self, repository: UserRepo) -> None:
        self.repository = repository


    def create (self, data: UserCreate) -> User:
        user = User(
            username=data.username,
            password=data.password,
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name if data.middle_name else None,
            is_active=data.is_active,
            is_staff=data.is_staff,
            is_superuser=data.is_superuser,

        )

        try:
            self.session.commit()

