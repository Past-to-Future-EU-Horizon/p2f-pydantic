from pydantic import BaseModel
from typing import Optional

class harm_location(BaseModel):
    pk_harm_location: Optional[int]
    fk_data_record: int
    latitude: float
    longitude: float
    location_age: int

class harm_data_species(BaseModel):
    pk_harm_species: Optional[int]
    fk_data_record: int
    genus_species: str