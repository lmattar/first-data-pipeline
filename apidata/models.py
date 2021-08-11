from typing_extensions import TypedDict
from sqlalchemy import Column, Integer, String , Float # type: ignore
from .database import Base
from sqlalchemy import PrimaryKeyConstraint


class MedalDict(TypedDict):
    year: float
    city: str
    sport: str
    discipline: str
    athlete: str
    country: str
    gender: str
    event: str
    medal: str

class Medal(Base):
    """
    Defines the items model
    """

    __tablename__ = "medals"
   
    year = Column(Float)
    city= Column(String)
    sport= Column(String)
    discipline= Column(String)
    athlete= Column(String)
    country= Column(String)
    gender= Column(String)
    event= Column(String)
    medal= Column(String)
    __table_args__ = (
        PrimaryKeyConstraint('year', 'discipline','athlete','event','medal'),
    )

    def __init__(self, year: float , city: str, sport: str, discipline: str, athlete: str, country: str, gender: str, event:str , medal: str ):
        self.year = year
        self.city = city
        self.sport = sport
        self.discipline = discipline
        self.athlete = athlete 
        self.country = country 
        self.gender = gender 
        self.event = event 
        self.medal = medal 

    def __repr__(self) -> str:
        return f"<Medal {self.year} {self.city} {self.athlete} {self.discipline} {self.event} {self.medal}>"

    @property
    def serialize(self) -> MedalDict:
        """
        Return item in serializeable format
        """
        return {"year": self.year, "city" : self.city  ,  "sport" : self.sport ,  "discipline" : self.discipline ,  "athlete" : self.athlete, "country" : self.country,   "gender" :self.gender , "event" : self.event, "medal" : self.medal }
