from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class OutageBase(BaseModel):
    start_time: datetime
    end_time: datetime
    description: str
    location: str

class OutageCreate(OutageBase):
    user_id: int = Field(..., description="ID del usuario asociado al corte")

class Outage(OutageBase):
    id: int
    user_id: Optional[int]  # Hacer que user_id sea opcional

    class Config:
        orm_mode = True
        from_attributes = True