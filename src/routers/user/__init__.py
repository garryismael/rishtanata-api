from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.config.container import Container
from src.domain.user.model import UserRegisterRequest
from src.domain.user.use_case import UserRegisterUseCase

user_router = APIRouter()


@user_router.post("/api/users", tags=["users"])
@inject
async def user_register(
    user_request: UserRegisterRequest,
    use_case: UserRegisterUseCase = Depends(Provide[Container.user_register]),
):
    return await use_case.execute(user_request)
