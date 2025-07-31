from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 🚗 Vehicle Schemas
class VehicleBase(BaseModel):
    plate_number: str
    model: str
    driver_name: str

class VehicleCreate(BaseModel):
    plate_number: str
    model: str
    driver_name: str

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id: int

    class Config:
        from_attributes = True

# 🚓 Patrol Schemas
class PatrolLogBase(BaseModel):
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    activity: Optional[str]= None
# --- PatrolLog Create ---
class PatrolLogCreate(PatrolLogBase):
    vehicle_id: int

# --- PatrolLog Read ---
class PatrolLog(PatrolLogBase):
    id: int
    vehicle_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# === PATROL LOG SCHEMAS ===
class PatrolBase(BaseModel):
    vehicle_id: int
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    activity: Optional[str]= None
    timestamp: datetime

class PatrolCreate(PatrolBase):
    pass

class Patrol(PatrolBase):
    id: int

    class Config:
        from_attributes = True
# 🚗 Vehicle Schema for nesting
class VehicleOut(BaseModel):
    id: int
    plate_number: str
    model: str
    driver_name: str

    class Config:
        from_attributes = True

# 🛡️ PatrolLog with nested vehicle
class PatrolLogOut(BaseModel):
    id: int
    vehicle_id: int
    location: str
    timestamp: datetime
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    activity: Optional[str] = None
    vehicle: VehicleOut

    class Config:
        from_attributes = True

# 🚓 Patrol GET with Vehicle Info
class PatrolLogOut(PatrolLogBase):
    id: int
    vehicle_id: int
    timestamp: datetime
    vehicle: Vehicle  # 👈 This includes the full vehicle details

    class Config:
        from_attributes = True
        
from typing import Optional
from pydantic import BaseModel

class PatrolWithVehicle(BaseModel):
    id: int
    vehicle_id: int
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    activity: Optional[str] = None
    timestamp: str
    vehicle: VehicleOut

    class Config:
        from_attributes = True   # Use this instead of `orm_mode`
