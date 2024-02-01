from enum import Enum

from pydantic import BaseModel

from src.domain.user.model import UserResponseDTO


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponseDTO

class TokenData(BaseModel):
    email: str
    action: str

class TokenAction(Enum):
    REGISTER = "register"
    PROFILE = "profile"
    ACCOUNT = "account"
    AUTH = "auth"