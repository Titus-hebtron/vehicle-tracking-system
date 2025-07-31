from sqlalchemy.orm import Session
from app import models, schemas


# === VEHICLES ===

def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def get_vehicles(db: Session):
    return db.query(models.Vehicle).all()

def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

def update_vehicle(db: Session, vehicle_id: int, vehicle_data: schemas.VehicleCreate):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not db_vehicle:
        return None

    for key, value in vehicle_data.dict().items():
        setattr(db_vehicle, key, value)

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()
    if not db_vehicle:
        return None

    db.delete(db_vehicle)
    db.commit()
    return True


# === PATROLS ===

def create_patrol(db: Session, patrol: schemas.PatrolCreate):
    db_patrol = models.PatrolLog(**patrol.dict())
    db.add(db_patrol)
    db.commit()
    db.refresh(db_patrol)
    return db_patrol

def get_patrols(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PatrolLog).offset(skip).limit(limit).all()

def get_patrol_by_id(db: Session, patrol_id: int):
    return db.query(models.PatrolLog).filter(models.PatrolLog.id == patrol_id).first()

def get_patrols_by_vehicle(db: Session, vehicle_id: int):
    return db.query(models.PatrolLog).filter(models.PatrolLog.vehicle_id == vehicle_id).all()

def update_patrol(db: Session, patrol_id: int, updated_data: schemas.PatrolCreate):
    patrol = db.query(models.PatrolLog).filter(models.PatrolLog.id == patrol_id).first()
    if not patrol:
        return None

    for key, value in updated_data.dict().items():
        setattr(patrol, key, value)

    db.commit()
    db.refresh(patrol)
    return patrol

def delete_patrol(db: Session, patrol_id: int):
    patrol = db.query(models.PatrolLog).filter(models.PatrolLog.id == patrol_id).first()
    if not patrol:
        return None

    db.delete(patrol)
    db.commit()
    return True

def create_patrol_log(db: Session, patrol_log: schemas.PatrolLogCreate):
    db_log = models.PatrolLog(**patrol_log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


def get_patrol_logs(db: Session):
    return db.query(models.PatrolLog).all()

def get_patrol_log_by_id(db: Session, log_id: int):
    return db.query(models.PatrolLog).filter(models.PatrolLog.id == log_id).first()

def delete_patrol_log(db: Session, log_id: int):
    log = get_patrol_log_by_id(db, log_id)
    if log:
        db.delete(log)
        db.commit()
        return True
    return False