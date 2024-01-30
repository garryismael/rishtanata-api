from dataclasses import dataclass
from typing import Optional


@dataclass
class Professional:
    occupation: str
    employer_name: str
    position_at_work: str
    father_occupation: str
    mother_occupation: str
    annual_income : Optional[int]
    personal_property_type: Optional[str]