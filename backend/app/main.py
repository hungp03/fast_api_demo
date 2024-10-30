from core.dbconfig import DBConfig
from fastapi import FastAPI
from models import User, Image, ProcessingJob
from api.main import api_router

app = FastAPI()
cfg = DBConfig()
cfg.create_tables()
app.include_router(api_router)



