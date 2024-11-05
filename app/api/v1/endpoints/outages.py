from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.outage import Outage, OutageCreate
from app.services.outage import OutageService

router = APIRouter()

@router.post("/", response_model=Outage)
def create_outage(outage: OutageCreate, db: Session = Depends(get_db)):
    created_outage = OutageService.create_outage(db=db, outage=outage)
    return created_outage

@router.get("/", response_model=List[Outage])
def read_outages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    outages = OutageService.get_outages(db, skip=skip, limit=limit)
    return outages

@router.get("/{outage_id}", response_model=Outage)
def read_outage(outage_id: int, db: Session = Depends(get_db)):
    outage = OutageService.get_outage(db, outage_id=outage_id)
    if outage is None:
        raise HTTPException(status_code=404, detail="Corte no encontrado")
    return outage

@router.patch("/{outage_id}", response_model=Outage)
def patch_outage(outage_id: int, outage: OutageCreate, db: Session = Depends(get_db)):
    db_outage = OutageService.get_outage(db, outage_id=outage_id)
    if db_outage is None:
        raise HTTPException(status_code=404, detail="Corte no encontrado")
    updated_outage = OutageService.patch_outage(db=db, outage_id=outage_id, outage=outage)
    return updated_outage

@router.delete("/{outage_id}", response_model=Outage)
def delete_outage(outage_id: int, db: Session = Depends(get_db)):
    db_outage = OutageService.get_outage(db, outage_id=outage_id)
    if db_outage is None:
        raise HTTPException(status_code=404, detail="Corte no encontrado")
    deleted_outage = OutageService.delete_outage(db=db, outage_id=outage_id)
    return deleted_outage