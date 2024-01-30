from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.config.container import Container
from src.domain.account.model import AccountRegistration
from src.domain.account.use_case import AccountCreationUseCase

account_router = APIRouter()


@account_router.post("/api/accounts/activate", tags=["accounts"])
@inject
async def activate_account(
    request: AccountRegistration,
    use_case: AccountCreationUseCase = Depends(Provide[Container.account_creation]),
):
    return await use_case.execute(request)
