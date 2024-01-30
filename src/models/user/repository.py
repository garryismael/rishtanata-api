from datetime import datetime

from src.constant import DATE_FORMAT
from src.domain.user.model import User, UserRegisterRequest
from src.models.user import UserModelMapper


class UserRepository:
    async def get_user_by_email(self, email: str):
        user = await UserModelMapper.get_or_none(email=email).prefetch_related(
            "account"
        )
        if user is not None:
            return user.cast()
        return None

    async def set_verification(self, user: User):
        user_db = await UserModelMapper.get(pk=user.id)
        user_db.verified = True
        await user_db.save()
        return user_db.cast()

    async def register(self, request: UserRegisterRequest) -> User:
        birthdate = datetime.strptime(request.birthdate, DATE_FORMAT)
        user_db = await UserModelMapper.create(
            full_name=request.full_name,
            gender=request.gender,
            birthdate=birthdate.date(),
            email=request.email,
            contact=request.contact,
        )
        return user_db.cast()
