from pydantic import BaseModel
from typing import Optional

class HARM_Rec_Age(BaseModel):
    fk_record_hash: str
    age_mean: int
    age_recent: Optional[int] = None
    age_oldest: Optional[int] = None
    reference_zero: int