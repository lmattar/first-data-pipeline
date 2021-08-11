from typing import List
from sqlalchemy.orm import Session  # type: ignore
from .models import Medal


#def get_item_by_name(session: Session, name: str) -> Medal:
#   return session.query(Item).filter(Item.name == name).first()

def get_medals(session: Session, skip: int = 0, limit: int = 100) -> List[Medal]:
    return session.query(Medal).offset(skip).limit(limit).all()