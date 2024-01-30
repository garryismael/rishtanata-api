from dataclasses import dataclass

from src.domain.account.model import AccountRegistration, UserAccount
from src.models.account.repository import AccountRepository
from src.utils import ApiException
from src.utils.auth import AuthService
from src.utils.token import UserTokenService


@dataclass
class AccountCreationUseCase:
    account_repository: AccountRepository
    user_token_service: UserTokenService
    exception: ApiException
    auth_service: AuthService

    async def execute(self, request: AccountRegistration):
        user = await self.user_token_service.get_user_by_token(request.token)
        if user.verified:
            self.exception.bad_request("User Already Verified")
        hashed_password = self.auth_service.get_password_hash(request.password)
        account = UserAccount(user=user, password=hashed_password)
        response = await self.account_repository.activate(account)
        return response
