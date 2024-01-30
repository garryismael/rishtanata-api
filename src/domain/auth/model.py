from pydantic import BaseModel
from src.domain.account.model import Account, AccountResponseDTO
from src.domain.user.model import User


class UserAccount(User):
    account: Account


class Token(BaseModel):
    access_token: str
    token_type: str
    account: AccountResponseDTO
