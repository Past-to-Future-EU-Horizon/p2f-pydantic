from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class harm_data_age(BaseModel):
    fk_record_hash: str
    age_mean: int
    age_recent: int
    age_oldest: int