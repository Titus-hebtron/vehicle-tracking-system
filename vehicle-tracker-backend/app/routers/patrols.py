from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from app import models, schemas
from app.database import get_db
from app.schemas import PatrolCreate, Patrol

router = APIRouter(prefix="/patrols", tags=["Patrol Logs"])

@router.post("/", response_model=Patrol)
def create_patrol(patrol: PatrolCreate, db: Session = Depends(get_db)):
    db_patrol = models.PatrolLog(**patrol.dict())
    db.add(db_patrol)
    db.commit()
    db.refresh(db_patrol)
    return db_patrol

@router.get("/", response_model=List[Patrol])
def get_all_patrols(db: Session = Depends(get_db)):
    return db.query(models.PatrolLog).all()

@router.get("/vehicle/{vehicle_id}", response_model=List[Patrol])
def get_patrols_by_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    return db.query(models.PatrolLog).filter(models.PatrolLog.vehicle_id == vehicle_id).all()

@router.get("/{patrol_id}", response_model=Patrol)
def get_patrol_by_id(patrol_id: int, db: Session = Depends(get_db)):
    patrol = db.query(models.PatrolLog).filter(models.PatrolLog.id == patrol_id).first()
    if not patrol:
        raise HTTPException(status_code=404, detail="Patrol log not found")
    return patrol

@router.put("/{patrol_id}", response_model=Patrol)
def update_patrol(patrol_id: int, updated: PatrolCreate, db: Session = Depends(get_db)):
    patrol = db.query(models.PatrolLog).filter(models.PatrolLog.id == patrol_id).first()
    if not patrol:
        raise HTTPException(status_code=404, detail="Patrol log not found")

    for key, value in updated.dict().items():
        setattr(patrol, key, value)

    db.commit()
    db.refresh(patrol)
    return patrol

@router.delete("/{patrol_id}")
def delete_patrol(patrol_id: int, db: Session = Depends(get_db)):
    patrol = db.query(models.PatrolLog).filter(models.PatrolLog.id == patrol_id).first()
    if not patrol:
        raise HTTPException(status_code=404, detail="Patrol log not found")

    db.delete(patrol)
    db.commit()
    return {"detail": "Patrol log deleted successfully"}

@router.get("/with-vehicles/", response_model=List[schemas.PatrolLogOut])
def get_patrol_logs(db: Session = Depends(get_db)):
    patrols = db.query(models.PatrolLog).options(joinedload(models.PatrolLog.vehicle)).all()
    return patrols
