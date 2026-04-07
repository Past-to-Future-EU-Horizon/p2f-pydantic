from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class HARM_Timeslice(BaseModel):
    timeslice_id: Optional[UUID] = None
    timeslice_name: str
    timeslice_age_mean: int
    timeslice_age_recent: Optional[int]
    timeslice_age_oldest: Optional[int]