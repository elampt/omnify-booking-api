from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

Base = declarative_base()

class FitnessClass(Base):
    __tablename__ = 'classes'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    datetime_ist = Column(DateTime, nullable=False)
    instructor = Column(String, nullable=False)
    total_slots = Column(Integer, nullable=False)
    available_slots = Column(Integer, nullable=False)

    bookings = relationship("Booking", back_populates="fitness_class")

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey('classes.id'), nullable=False)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)

    fitness_class = relationship("FitnessClass", back_populates="bookings")