from pydantic import BaseModel
from src.domain.account.model import Account
from src.domain.user.model import User, UserResponseDTO


class UserAccount(User):
    account: Account


class Token(BaseModel):
    access_token: str
    token_type: str
    account: UserResponseDTO