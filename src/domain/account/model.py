from pydantic import BaseModel, Field, model_validator

from src.domain.user.model import User


class Account(BaseModel):
    id: int
    user: User
    password: str
    created_at: str
    updated_at: str

    @property
    def dto(self) -> "AccountResponseDTO":
        return AccountResponseDTO(
            id=self.id,
            user=self.user,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


class AccountRequest(BaseModel):
    password: str = Field(..., min_length=5)
    user: User


class AccountRegistration(BaseModel):
    token: str
    password: str = Field(..., min_length=5)
    confirm_password: str = Field(..., min_length=5)

    @model_validator(mode="after")
    def check_passwords_match(self) -> "AccountRegistration":
        password = self.password
        confirm_password = self.confirm_password
        if (
            password is not None
            and confirm_password is not None
            and password != confirm_password
        ):
            raise ValueError("passwords do not match")
        return self


class UserAccount(BaseModel):
    user: User
    password: str


class AccountResponseDTO(BaseModel):
    id: int
    user: User
    created_at: str
    updated_at: str
