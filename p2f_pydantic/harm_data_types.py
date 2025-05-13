from pydantic import BaseModel
from typing import Optional

class harm_data_type(BaseModel):
    pk_harm_data_type: Optional[int]
    measure: str
    method: str