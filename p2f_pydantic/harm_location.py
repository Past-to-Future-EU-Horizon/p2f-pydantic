from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

class HARM_Location(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    location_id: Optional[UUID] = None
    location_name: Optional[str] = None
    location_code: Optional[str] = None
    latitude: float
    longitude: float
    elevation: float
    location_age: int

class HARM_Bounding_Box(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    north: float
    east: float
    south: float
    west: float