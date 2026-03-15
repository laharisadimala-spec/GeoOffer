from database import SessionLocal
import models

db = SessionLocal()

# ---------- STORES ----------
store1 = models.Store(
    name="Cafe Aroma",
    latitude=17.3850,
    longitude=78.4867
)

store2 = models.Store(
    name="StyleMart",
    latitude=17.3855,
    longitude=78.4870
)

db.add_all([store1, store2])
db.commit()

# ---------- OFFERS ----------
offer1 = models.Offer(
    title="20% OFF Coffee",
    category="Coffee & Beverages",
    store_id=1,
    discount="20%"
)

offer2 = models.Offer(
    title="15% OFF Sneakers",
    category="Fashion",
    store_id=2,
    discount="15%"
)

db.add_all([offer1, offer2])
db.commit()

print("Database seeded successfully")