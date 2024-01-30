from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.config.container import Container
from src.domain.auth.use_case import UserLoginUseCase

auth_router = APIRouter()


@auth_router.post("/api/auth/token", tags=["auth"])
@inject
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    use_case: UserLoginUseCase = Depends(Provide[Container.user_login]),
):
    return await use_case.execute(form_data.username, form_data.password)
