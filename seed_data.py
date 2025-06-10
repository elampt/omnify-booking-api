from models import FitnessClass
from datetime import datetime, timedelta

def seed_classes(db):
    if db.query(FitnessClass).count() > 0:
        return  # Already seeded
    now = datetime.now()
    classes = [
        FitnessClass(
            name="Yoga",
            datetime_ist=now + timedelta(days=1, hours=7),
            instructor="Alice",
            total_slots=10,
            available_slots=10
        ),
        FitnessClass(
            name="Zumba",
            datetime_ist=now + timedelta(days=2, hours=9),
            instructor="Bob",
            total_slots=15,
            available_slots=15
        ),
        FitnessClass(
            name="HIIT",
            datetime_ist=now + timedelta(days=3, hours=18),
            instructor="Charlie",
            total_slots=12,
            available_slots=12
        ),
    ]
    db.add_all(classes)
    db.commit()