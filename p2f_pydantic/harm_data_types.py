from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class HARM_Data_Type(BaseModel):
    datatype_id: Optional[UUID] = None
    measure: str
    unit_of_measurement: str
    method: Optional[str] = None
    is_proxy: bool