from pydantic import BaseModel
from typing import Optional

class harm_data_type(BaseModel):
    pk_harm_data_type: Optional[int] = None
    measure: str
    unit_of_measurement: str
    method: Optional[str]
    is_proxy: bool