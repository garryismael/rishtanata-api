from dataclasses import dataclass

from passlib.context import CryptContext

from src.models.account.repository import AccountRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@dataclass
class AuthService:
    account_repository: AccountRepository

    def verify_password(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return pwd_context.hash(password)

    async def authenticate_user(self, email: str, password: str):
        account = await self.account_repository.get_account_by_email(email)
        if account is None:
            return None
        if not self.verify_password(password, account.password):
            return None
        return account.dto