from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas, database

router = APIRouter(
    prefix="/patrol-logs",
    tags=["Patrol Logs"]
)

@router.post("/", response_model=schemas.Patrol)
def create_patrol_log(patrol_log: schemas.PatrolCreate, db: Session = Depends(database.get_db)):
    return crud.create_patrol_log(db, patrol_log)

@router.get("/", response_model=List[schemas.Patrol])
def read_patrol_logs(db: Session = Depends(database.get_db)):
    return crud.get_patrol_logs(db)

@router.get("/{log_id}", response_model=schemas.Patrol)
def read_patrol_log(log_id: int, db: Session = Depends(database.get_db)):
    log = crud.get_patrol_log_by_id(db, log_id)
    if log is None:
        raise HTTPException(status_code=404, detail="Patrol log not found")
    return log

@router.delete("/{log_id}", response_model=dict)
def delete_patrol_log(log_id: int, db: Session = Depends(database.get_db)):
    success = crud.delete_patrol_log(db, log_id)
    if not success:
        raise HTTPException(status_code=404, detail="Patrol log not found")
    return {"message": "Patrol log deleted"}
