from datetime import datetime
from pydantic import ConfigDict
from pydantic import BaseModel, Field, EmailStr

class ClassResponse(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    model_config = ConfigDict(from_attributes=True)

class BookingRequest(BaseModel):
    class_id: int
    client_name: str = Field(..., min_length=1)
    client_email: EmailStr

class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
    class_name: str
    datetime: datetime
    instructor: str

    model_config = ConfigDict(from_attributes=True)