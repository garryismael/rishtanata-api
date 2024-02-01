from typing import Optional

from pydantic import BaseModel, EmailStr, Field, model_validator


class User(BaseModel):
    id: int
    full_name: str
    birthdate: str
    birth_city: Optional[str] = None
    birth_country: Optional[str] = None
    gender: str
    address: Optional[str] = None
    email: EmailStr
    cell_phone: str
    home_phone: Optional[str] = None
    photo: Optional[str] = None
    nationality: Optional[str] = None
    ethnic_group: Optional[str] = None
    marital_status: Optional[str] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    complexion: Optional[str] = None
    occupation: Optional[str] = None
    verified: bool
    profile_active: bool
    password: Optional[str] = None
    is_admin: bool


class UserRegisterRequest(BaseModel):
    full_name: str
    gender: str
    birthdate: str
    email: EmailStr
    cell_phone: str


class UserResponseDTO(BaseModel):
    id: int
    full_name: str
    birthdate: str
    birth_city: Optional[str] = None
    birth_country: Optional[str] = None
    gender: str
    address: Optional[str] = None
    email: EmailStr
    cell_phone: str
    home_phone: Optional[str] = None
    photo: Optional[str] = None
    nationality: Optional[str] = None
    ethnic_group: Optional[str] = None
    marital_status: Optional[str] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    complexion: Optional[str] = None
    occupation: Optional[str] = None
    verified: bool
    profile_active: bool
    password: Optional[str] = None
    is_admin: bool


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