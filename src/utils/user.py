from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.config.container import Container
from src.utils.token import UserTokenService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@inject
async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_token_service: UserTokenService = Depends(
        Provide[Container.user_token_service]),
):
    return user_token_service.get_user_by_token(token)
