from dataclasses import dataclass

from src.domain.user.model import User, UserRegisterRequest
from src.models.user.repository import UserRepository


@dataclass
class UserService:
    user_repository: UserRepository

    async def register(self, request: UserRegisterRequest) -> User:
        user_db = await self.user_repository.save(request)
        return user_db.cast()
