from sqlalchemy.orm import Session
from app.models.outage import Outage as OutageModel
from app.schemas.outage import OutageCreate

class OutageService:
    def create_outage(db: Session, outage: OutageCreate):
        db_outage = OutageModel(
            start_time=outage.start_time,
            end_time=outage.end_time,
            description=outage.description,
            location=outage.location
     )
        db.add(db_outage)
        db.commit()
        db.refresh(db_outage)
        return db_outage

    def get_outages(db: Session, skip: int = 0, limit: int = 100)   :
        return db.query(OutageModel).offset(skip).limit(limit).all()

    def get_outage(db: Session, outage_id: int):
     return db.query(OutageModel).filter(OutageModel.id == outage_id).first()
 
    def patch_outage(db: Session, outage_id: int, outage: OutageCreate):
        db_outage = db.query(OutageModel).filter(OutageModel.id == outage_id).first()
        db_outage.start_time = outage.start_time
        db_outage.end_time = outage.end_time
        db_outage.description = outage.description
        db_outage.location = outage.location
        db.commit()
        db.refresh(db_outage)
        return db_outage
    
    def delete_outage(db: Session, outage_id: int):
        db_outage = db.query(OutageModel).filter(OutageModel.id == outage_id).first()
        db.delete(db_outage)
        db.commit()
        return db_outage