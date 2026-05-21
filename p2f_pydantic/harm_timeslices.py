from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

class HARM_Timeslice(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    timeslice_id: Optional[UUID] = None
    timeslice_name: str
    timeslice_age_mean: int
    timeslice_age_recent: Optional[int]
    timeslice_age_oldest: Optional[int]