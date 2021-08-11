from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore
from fastapi.responses import JSONResponse
from . import crud, models
from .database import SessionLocal, engine
from .schemas import MedalBase, Top10Base
import pandas as pd

models.Base.metadata.create_all(bind=engine)
itemrouter = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@itemrouter.get("/medals/", response_model=List[MedalBase])
def read_medals(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    medals = crud.get_medals(session=session, skip=skip, limit=limit)
    return [i.serialize for i in medals]


@itemrouter.get("/top10/")
def read_top10(session: Session = Depends(get_session)):
    sql_df = pd.read_sql("select country, count(*) as Medals from public.medals group by country order by count(*) desc limit 10",con=engine )
    print(sql_df.to_json()) 
    return   JSONResponse(content=sql_df.to_json(orient="records")) 
