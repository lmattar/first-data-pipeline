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
    return   JSONResponse(content=sql_df.to_dict(orient="records")) 

@itemrouter.get("/top3disciplines/")
def read_top10(session: Session = Depends(get_session)):
    sql_df = pd.read_sql("select country,discipline, count(*) as medals from medals where country in ( select country  from public.medals group by country order by count(*) desc limit 3) group by country,discipline order by country,count(*) desc ",con=engine )
    print(sql_df.to_json()) 
    return   JSONResponse(content=sql_df.to_dict(orient="row")) 


@itemrouter.get("/medalsbyyear/")
def read_top10(session: Session = Depends(get_session)):
    sql_df = pd.read_sql("select  year, count(*) as medallas from medals group by year order by count(*) desc",con=engine )
    print(sql_df.to_json()) 
    return   JSONResponse(content=sql_df.to_dict(orient="row")) 

@itemrouter.get("/medalsbytype/")
def read_top10(session: Session = Depends(get_session)):
    sql_df = pd.read_sql("select medal , count(*) from medals group by medal",con=engine )
    print(sql_df.to_json()) 
    return   JSONResponse(content=sql_df.to_dict(orient="row")) 

@itemrouter.get("/disciplines/")
def read_top10(session: Session = Depends(get_session)):
    sql_df = pd.read_sql(""" select t.athlete, count(*)
                        from (
                                select athlete , discipline, count(*) 
                                from medals 
                                group by athlete , discipline   
                            ) as t
                        group by athlete
                        having count(*)>1
                        order by count(*) desc
                        """,con=engine )
    print(sql_df.to_json()) 
    return   JSONResponse(content=sql_df.to_dict(orient="row")) 


