from pydantic import BaseModel

class InformationBase(BaseModel):
    family_background_note: str
    expectation_note: str
    wears_coat: bool
    wears_hijab: bool
    willingness_to_relocate: str
    preferred_living_arrangement: str
    health_note: str


class Information(InformationBase):
    id: int
