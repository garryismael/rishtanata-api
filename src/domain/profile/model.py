from dataclasses import dataclass

from src.domain.user.model import User

@dataclass
class Profile:
    id: str
    address: str
    father_name: str
    mother_name: str
    nationality: str
    ethnic_group: str
    martial_status: str
    user: User
    approved: bool = False