from dataclasses import dataclass
from typing import Optional
from typing_extensions import Annotated
from fastapi import Form

from pydantic import BaseModel, EmailStr, Field, model_validator

from src.domain.information.model import Information


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
    information: Optional[Information] = None


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
    information: Optional[Information] = None

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

@dataclass
class ProfileUpdateRequest():
    full_name: Annotated[str, Form()]
    birthdate: Annotated[str, Form()]
    gender: Annotated[str, Form()]
    email: Annotated[str, Form()]
    cell_phone: Annotated[str, Form()]
    health_note: Annotated[str, Form()]
    family_background_note: Annotated[str, Form()]
    expectation_note: Annotated[str, Form()]
    wears_coat: Annotated[bool, Form()]
    willingness_to_relocate: Annotated[str, Form()]
    preferred_living_arrangement: Annotated[str, Form()]
    wears_hijab: Annotated[bool, Form()]
    is_admin: Annotated[bool, Form()] = False
    birth_city: Annotated[Optional[str], Form()] = None
    birth_country: Annotated[Optional[str], Form()] = None
    address: Annotated[Optional[str], Form()] = None
    home_phone: Annotated[Optional[str], Form()] = None
    photo: Annotated[Optional[str], Form()] = None
    nationality: Annotated[Optional[str], Form()] = None
    ethnic_group: Annotated[Optional[str], Form()] = None
    marital_status: Annotated[Optional[str], Form()] = None
    height: Annotated[int, Form()] = None
    weight: Annotated[int, Form()] = None
    complexion: Annotated[Optional[str], Form()] = None
    occupation: Annotated[Optional[str], Form()] = None
