from dataclasses import dataclass
from src.config.app import APP_CONFIG
from src.domain.token import TokenAction
from src.domain.user.model import UserRegisterRequest, UserResponseDTO
from src.models.user.repository import UserRepository
from src.utils.email import MailService
from src.utils.token.factory import AccessTokenFactory

REGISTER_SUBJECT = "User Verification"


@dataclass
class UserRegisterUseCase:
    user_repository: UserRepository
    access_token_factory: AccessTokenFactory
    mail_service: MailService

    async def execute(self, request: UserRegisterRequest) -> UserResponseDTO:
        user = await self.user_repository.register(request)
        data = {
            "id": f"{user.id}",
            "full_name": user.full_name,
            "sub": user.email,
            "action": TokenAction.REGISTER.value,
        }
        jwt = self.access_token_factory.create_access_token(data)
        body = {
            "subject": REGISTER_SUBJECT,
            "full_name": user.full_name,
            "url": f"{APP_CONFIG.website_url}/email-verify/{jwt}",
            "emails": [user.email],
        }
        print(jwt)
        # await self.mail_service.send(
        #     REGISTER_SUBJECT,
        #     body,
        #     "verification.html",
        # )

        return UserResponseDTO(**user.model_dump())
