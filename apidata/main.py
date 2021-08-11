from fastapi import FastAPI
from .routers import itemrouter
from .database import engine
import pandas as pd


app = FastAPI()
app.include_router(itemrouter)
