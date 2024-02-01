from dataclasses import dataclass

from src.config.app import APP_CONFIG
from src.domain.auth.model import TokenAction
from src.domain.user.model import (
    AccountRegistration,
    UserRegisterRequest,
    UserResponseDTO,
)
from src.models.user.repository import UserRepository
from src.models.user.service import UserService
from src.utils import ApiException
from src.utils.auth import AuthService
from src.utils.email import MailService
from src.utils.token import UserTokenService
from src.utils.token.factory import AccessTokenFactory

REGISTER_SUBJECT = "User Verification"


@dataclass
class UserRegisterUseCase:
    user_service: UserService
    access_token_factory: AccessTokenFactory
    mail_service: MailService

    async def execute(self, request: UserRegisterRequest) -> UserResponseDTO:
        user = await self.user_service.register(request)
        data = {
            "id": f"{user.id}",
            "full_name": user.full_name,
            "sub": user.email,
            "action": TokenAction.REGISTER.value,
            "is_admin": user.is_admin,
        }
        jwt = self.access_token_factory.create_access_token(data)
        body = {
            "subject": REGISTER_SUBJECT,
            "full_name": user.full_name,
            "url": f"{APP_CONFIG.website_url}/email-verify/{jwt}",
            "emails": [user.email],
        }
        await self.mail_service.send(
            REGISTER_SUBJECT,
            body,
            "verification.html",
        )

        return UserResponseDTO(**user.model_dump())


@dataclass
class AccountCreationUseCase:
    user_repository: UserRepository
    user_token_service: UserTokenService
    exception: ApiException
    auth_service: AuthService

    async def execute(self, request: AccountRegistration):
        user = await self.user_token_service.get_user_by_token(request.token)
        if user.verified:
            self.exception.bad_request("User Already Verified")
        hashed_password = self.auth_service.get_password_hash(request.password)
        user.password = hashed_password
        user.verified = True
        return UserResponseDTO(**user.model_dump())
