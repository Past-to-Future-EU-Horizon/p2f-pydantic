from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

class HARM_Data_Type(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    datatype_id: Optional[UUID] = None
    measure: str
    unit_of_measurement: str
    method: Optional[str] = None
    calibration: Optional[str] = None
    is_proxy: bool