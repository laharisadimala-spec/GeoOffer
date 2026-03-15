from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class PreferenceCreate(BaseModel):
    user_id: int
    category: str


class OfferResponse(BaseModel):
    title: str
    category: str
    discount: str