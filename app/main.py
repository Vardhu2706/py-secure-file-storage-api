# Main.py

# Imports
from fastapi import FastAPI
from app.db.session import SessionLocal, engine
from app.models import user_model, file_model 


app = FastAPI()

import app.models.user_model
import app.models.file_model

