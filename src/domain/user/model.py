from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    full_name: str
    gender: str
    birthdate: str
    birth_country: Optional[str] = str
    email: EmailStr
    contact: str
    photo: Optional[str]
    verified: bool
    created_at: str
    updated_at: str


class UserRegisterRequest(BaseModel):
    full_name: str
    gender: str
    birthdate: str
    email: EmailStr
    contact: str


class UserResponseDTO(BaseModel):
    id: int
    full_name: str
    gender: str
    birthdate: str
    birth_country: Optional[str] = str
    email: EmailStr
    contact: str
    photo: Optional[str]
    verified: bool
    created_at: str
