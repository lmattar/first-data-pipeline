import os
import time
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore

time.sleep(100)
host = "pg_container" #os.environ["POSTGRES_HOST"]
port = 5432 #os.environ["POSTGRES_PORT"]
user = "postgres" #os.environ["POSTGRES_USER"]
password = "postgres" #os.environ["POSTGRES_PASS"]
db = "jjoo" #os.environ["POSTGRES_DB"]
dbtype = "postgresql"

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password }@{host}:{port}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
