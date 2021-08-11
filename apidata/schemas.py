from pydantic import BaseModel


class MedalBase(BaseModel):
    year: float
    city: str
    sport: str
    discipline: str
    athlete: str
    country: str
    gender: str
    event: str
    medal: str

class Top10Base(BaseModel):
    country: str
    count: float