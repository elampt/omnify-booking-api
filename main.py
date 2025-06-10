from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from database import initialize_database, get_db
from crud import get_class, book_class, get_bookings
from schemas import ClassResponse, BookingRequest, BookingResponse
from typing import List
from fastapi import Depends
from contextlib import asynccontextmanager
import logging

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize the database on startup."""
    initialize_database()
    yield

app = FastAPI(title = "Fitness Studio Booking API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/classes", response_model=List[ClassResponse])
def read_classes(timezone: str = Query("Asia/Kolkata", description="Timezone for class timings")):
    logger.info(f"Fetching classes for timezone: {timezone}")
    db = Depends(get_db())
    return get_class(db, timezone)

@app.post("/book", response_model = BookingResponse)
def create_booking(booking_request: BookingRequest):
    logger.info(f"Booking request received: {booking_request}")
    db = Depends(get_db())
    try:
        result = book_class(db, booking_request)
        logger.info(f"Booking successful for {booking_request.client_name}")
        return result
    except ValueError as e:
        logger.warning(f"Booking failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/bookings", response_model=List[BookingResponse])
def read_bookings(client_email: str = Query(..., description="Client email to fetch bookings")):
    logger.info(f"Fetching bookings for email: {client_email}")
    db = Depends(get_db())
    return get_bookings(db, client_email)