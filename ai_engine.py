import pandas as pd

def recommend_offers(user_preferences, offers):

    recommended = []

    for offer in offers:
        if offer.category in user_preferences:
            recommended.append({
                "title": offer.title,
                "reason": f"Recommended because you selected {offer.category}"
            })

    return recommended