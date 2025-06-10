from models import FitnessClass, Booking
from schemas import BookingRequest, BookingResponse, ClassResponse
from sqlalchemy.orm import Session
from utils.timezone import convert_ist_to_timezone
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def get_class(db: Session, timezone: str):
    classes = db.query(FitnessClass).filter(FitnessClass.datetime_ist > datetime.now()).all()
    result = []
    for c in classes:
        dt = convert_ist_to_timezone(c.datetime_ist, timezone)
        result.append(ClassResponse(
            id=c.id,
            name=c.name,
            datetime=dt,
            instructor=c.instructor,
            available_slots=c.available_slots
        ))
    return result

def book_class(db: Session, booking_request: BookingRequest):
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == booking_request.class_id).first()
    if not fitness_class:
        logger.error(f"Class with ID {booking_request.class_id} not found")
        return None  # Class not found
    if fitness_class.available_slots <= 0:
        logger.error(f"No available slots for class ID {booking_request.class_id}")
        raise ValueError("No available slots for this class")
    # Prevent duplicate bookings for the same class and email
    existing = db.query(Booking).filter(
        Booking.class_id == booking_request.class_id,
        Booking.client_email == booking_request.client_email
    ).first()
    if existing:
        logger.warning(f"Duplicate booking attempt for class ID {booking_request.class_id} by {booking_request.client_email}")
        raise ValueError("You have already booked this class")
    
    booking = Booking(
        class_id=booking_request.class_id,
        client_name=booking_request.client_name,
        client_email=booking_request.client_email
    )
    fitness_class.available_slots -= 1
    db.add(booking)
    db.commit()
    return BookingResponse(
        id=booking.id,
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email,
        class_name=fitness_class.name,
        datetime=fitness_class.datetime_ist,
        instructor=fitness_class.instructor
    )

def get_bookings(db: Session, client_email: str):
    bookings = db.query(Booking).filter(Booking.client_email == client_email).all()
    if not bookings:
        logger.info(f"No bookings found for email: {client_email}")
        return []  # No bookings found for this email
    result = []
    for b in bookings:
        fc = db.query(FitnessClass).filter(FitnessClass.id == b.class_id).first()
        result.append(BookingResponse(
            id=b.id,
            class_id=b.class_id,
            client_name=b.client_name,
            client_email=b.client_email,
            class_name=fc.name,
            datetime=fc.datetime_ist,
            instructor=fc.instructor
        ))
    return result