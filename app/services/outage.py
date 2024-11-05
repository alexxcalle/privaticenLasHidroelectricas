from sqlalchemy.orm import Session
from app.models.outage import Outage as OutageModel
from app.schemas.outage import OutageCreate, Outage
from typing import List

class OutageService:
    @staticmethod
    def create_outage(db: Session, outage: OutageCreate) -> Outage:
        db_outage = OutageModel(
            start_time=outage.start_time,
            end_time=outage.end_time,
            description=outage.description,
            location=outage.location,
            user_id=outage.user_id
        )
        db.add(db_outage)
        db.commit()
        db.refresh(db_outage)
        return Outage.from_orm(db_outage)

    @staticmethod
    def get_outages(db: Session, skip: int = 0, limit: int = 100) -> List[Outage]:
        outages = db.query(OutageModel).offset(skip).limit(limit).all()
        return [Outage.from_orm(outage) for outage in outages]

    @staticmethod
    def get_outage(db: Session, outage_id: int) -> Outage:
        outage = db.query(OutageModel).filter(OutageModel.id == outage_id).first()
        if outage:
            return Outage.from_orm(outage)
        return None

    @staticmethod
    def patch_outage(db: Session, outage_id: int, outage: OutageCreate) -> Outage:
        db_outage = db.query(OutageModel).filter(OutageModel.id == outage_id).first()
        if db_outage:
            db_outage.start_time = outage.start_time
            db_outage.end_time = outage.end_time
            db_outage.description = outage.description
            db_outage.location = outage.location
            db_outage.user_id = outage.user_id
            db.commit()
            db.refresh(db_outage)
            return Outage.from_orm(db_outage)
        return None

    @staticmethod
    def delete_outage(db: Session, outage_id: int) -> Outage:
        db_outage = db.query(OutageModel).filter(OutageModel.id == outage_id).first()
        if db_outage:
            db.delete(db_outage)
            db.commit()
            return Outage.from_orm(db_outage)
        return None