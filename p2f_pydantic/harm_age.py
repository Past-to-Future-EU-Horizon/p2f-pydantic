from pydantic import BaseModel, ConfigDict
from typing import Optional

class HARM_Rec_Age(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fk_record_hash: str
    age_mean: int
    age_recent: Optional[int] = None
    age_oldest: Optional[int] = None
    reference_zero: int