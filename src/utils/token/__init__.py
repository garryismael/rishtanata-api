from dataclasses import dataclass

from jose import JWTError, jwt

from src.config.app import APP_CONFIG
from src.constant import CREDENTIALS_EXCEPTION
from src.models.user.repository import UserRepository


@dataclass
class UserTokenService:
    user_repository: UserRepository

    async def get_user_by_token(self, token: str):
        try:
            payload = jwt.decode(
                token, APP_CONFIG.secret_key, algorithms=[APP_CONFIG.algorithm]
            )
            email: str = payload.get("sub")
            if email is None:
                raise CREDENTIALS_EXCEPTION
        except JWTError:
            raise CREDENTIALS_EXCEPTION
        user = await self.user_repository.get_user_by_email(email=email)
        if user is None:
            raise CREDENTIALS_EXCEPTION
        return user.cast()
