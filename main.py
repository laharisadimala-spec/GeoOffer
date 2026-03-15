from fastapi import FastAPI
import models
from database import engine

from routers import auth, offers, recommendations

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Retail AI Offer System")

app.include_router(auth.router)
app.include_router(offers.router)
app.include_router(recommendations.router)


@app.get("/")
def root():
    return {"message": "Backend running successfully"}