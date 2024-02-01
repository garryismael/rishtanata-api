from dataclasses import dataclass

from passlib.context import CryptContext
from src.domain.user.model import UserResponseDTO

from src.models.user.repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@dataclass
class AuthService:
    user_repository: UserRepository

    def verify_password(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return pwd_context.hash(password)

    async def authenticate_user(self, email: str, password: str):
        user = await self.user_repository.get_user_by_email(email)
        if user is None or not self.verify_password(password, user.password):
            return None
        return UserResponseDTO(user.cast().model_dump())
