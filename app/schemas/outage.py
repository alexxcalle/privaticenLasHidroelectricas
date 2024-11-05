from datetime import datetime
from pydantic import BaseModel

class OutageBase(BaseModel):
    start_time: datetime
    end_time: datetime
    description: str
    location: str

class OutageCreate(OutageBase):
    pass

class Outage(OutageBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True