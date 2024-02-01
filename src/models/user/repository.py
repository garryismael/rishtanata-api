from datetime import datetime

from src.constant import DATE_FORMAT
from src.domain.user.model import User, UserRegisterRequest
from src.models.user import UserModelMapper


class UserRepository:
    async def get_user_by_email(self, email: str):
        user = await UserModelMapper.get_or_none(email=email)
        return user if user is not None else None

    async def save(self, request: UserRegisterRequest):
        birthdate = datetime.strptime(request.birthdate, DATE_FORMAT).date()
        user_db = await UserModelMapper.create(
            full_name=request.full_name,
            gender=request.gender,
            birthdate=birthdate,
            email=request.email,
            cell_phone=request.cell_phone,
        )
        return user_db

    async def activate(self, user_id: int, hashed_password: str):
        user_db = await UserModelMapper.get(pk=user_id)
        user_db.password = hashed_password
        user_db.verified = True
        await user_db.save()
        return user_db.cast()