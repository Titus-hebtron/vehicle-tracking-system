from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, unique=True, index=True, nullable=False)
    driver_name = Column(String, nullable=False)
    model = Column(String)
    
    
    # Relationship to PatrolLog
    patrol_logs = relationship("PatrolLog", back_populates="vehicle")


class PatrolLog(Base):
    __tablename__ = "patrol_logs"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    activity = Column(String)

    # Relationship to Vehicle
    vehicle = relationship("Vehicle", back_populates="patrol_logs")
