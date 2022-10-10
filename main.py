from fastapi import FastAPI

from models import *
from databases import migration 

app = FastAPI()

from routes import route