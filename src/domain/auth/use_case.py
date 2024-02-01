from dataclasses import dataclass
from datetime import timedelta

from src.config.app import AppConfig
from src.domain.auth.model import Token, TokenAction
from src.utils import ApiException
from src.utils.auth import AuthService
from src.utils.token.factory import AccessTokenFactory


@dataclass
class UserLoginUseCase:
    auth_service: AuthService
    exception: ApiException
    app_config: AppConfig
    access_token_factory: AccessTokenFactory

    async def execute(self, email: str, password: str):
        user = await self.auth_service.authenticate_user(email, password)
        if user is None:
            self.exception.unauthorized("Incorrect username or password")

        access_token_expires = timedelta(
            minutes=self.app_config.access_token_expire_minutes
        )
        data = {
            "id": f"{user.id}",
            "full_name": user.full_name,
            "sub": user.email,
            "action": TokenAction.AUTH.value,
            "is_admin": user.is_admin
        }
        access_token = self.access_token_factory.create_access_token(
            data=data, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer", user=user)
