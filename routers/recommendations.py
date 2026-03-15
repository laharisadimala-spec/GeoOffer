from fastapi import APIRouter

router = APIRouter()

@router.get("/recommend/{user_id}")
def get_recommendations(user_id: int):
    return {
        "user_id": user_id,
        "recommended_offers": [
            {
                "offer": "10% OFF Coffee",
                "reason": "Based on Coffee & Beverages preference"
            },
            {
                "offer": "15% OFF Sneakers",
                "reason": "Based on Fashion preference"
            }
        ]
    }