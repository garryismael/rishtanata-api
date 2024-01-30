from dataclasses import dataclass

from src.domain.account.model import UserAccount
from src.models.account import AccountModelMapper
from src.models.user.repository import UserRepository


@dataclass
class AccountRepository:
    user_repository: UserRepository

    async def get_account_by_email(self, email: str):
        model = await AccountModelMapper.get_or_none(
            user__email=email
        ).prefetch_related("user")
        return model.account if model is not None else None

    async def activate(self, account: UserAccount):
        await self.user_repository.set_verification(account.user)
        account_db = await AccountModelMapper.create(
            user_id=account.user.id, password=account.password
        )
        await account_db.fetch_related("user")
        return account_db.cast()
