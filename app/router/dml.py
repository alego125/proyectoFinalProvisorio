from fastapi import APIRouter, Depends, status
from app.schemas import *
from app.db.database import get_db
from typing import List
from sqlalchemy.orm import Session
from app.repositiry import user

# Definimos nuestro router
router = APIRouter(
    prefix = "/user",
    tags = ["Users"]
)