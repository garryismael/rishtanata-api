from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.config.container import Container
from src.domain.user.model import AccountRegistration, UserRegisterRequest
from src.domain.user.use_case import (AccountCreationUseCase,
                                      UserRegisterUseCase)

user_router = APIRouter()


@user_router.post("/api/users", tags=["users"])
@inject
async def user_register(
    user_request: UserRegisterRequest,
    use_case: UserRegisterUseCase = Depends(Provide[Container.user_register]),
):
    return await use_case.execute(user_request)


@user_router("/api/users/activate")
@inject
async def activate_account(
    request: AccountRegistration,
    use_case: AccountCreationUseCase = Depends(
        Provide[Container.account_creation]),
):
    return await use_case.execute(request)
