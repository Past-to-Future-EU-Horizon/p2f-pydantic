from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class HARM_Location(BaseModel):
    location_id: Optional[UUID] = None
    location_name: Optional[str] = None
    location_code: Optional[str] = None
    latitude: float
    longitude: float
    elevation: float
    location_age: int

class HARM_Bounding_Box(BaseModel):
    north: float
    east: float
    south: float
    west: float