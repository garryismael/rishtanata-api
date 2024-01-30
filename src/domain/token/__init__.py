from enum import Enum
from pydantic import BaseModel


class TokenData(BaseModel):
    email: str
    action: str

class TokenAction(Enum):
    REGISTER = "register"
    PROFILE = "profile"
    ACCOUNT = "account"
    AUTH = "auth"