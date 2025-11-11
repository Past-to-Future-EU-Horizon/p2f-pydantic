from pydantic import BaseModel
from typing import Optional

class harm_data_type(BaseModel):
    measure: str
    unit_of_measurement: str
    method: Optional[str]
    is_proxy: bool