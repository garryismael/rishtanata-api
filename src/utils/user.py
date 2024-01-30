from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.config.container import Container
from src.domain.account.model import AccountRegistration, AccountRequest
from src.utils.token import UserTokenService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@inject
async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_token_service: UserTokenService = Depends(
        Provide[Container.user_token_service]
    ),
):
    return user_token_service.get_user_by_token(token)


async def get_unverified_user(
    account_registration: AccountRegistration,
    user_token_service: UserTokenService = Depends(
        Provide[Container.user_token_service]
    ),
):
    user = await user_token_service.get_user_by_token(account_registration.token)
    if user.verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Account already verified"
        )
    request = AccountRequest(password=account_registration.password, user=user)
    return request
