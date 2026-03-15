from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/offers")
def get_offers(db: Session = Depends(get_db)):

    offers = db.query(models.Offer).all()

    return offers