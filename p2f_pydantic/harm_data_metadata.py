from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class HARM_Location(BaseModel):
    location_identifier: Optional[UUID] = None
    location_name: Optional[str] = None
    location_code: Optional[str] = None
    latitude: float
    longitude: float
    elevation: float
    location_age: int

class HARM_Location_to_Record(BaseModel):
    fk_harm_location: UUID
    fk_data_record: str

class HARM_Bounding_Box(BaseModel):
    north: float
    east: float
    south: float
    west: float

class HARM_Data_Species(BaseModel):
    species_identifier: Optional[UUID] = None
    display_species: str
    common_name: Optional[str] = None
    tax_domain: Optional[str] = None
    tax_kingdom: Optional[str] = None
    tax_subkingdom: Optional[str] = None
    tax_infrakingdom: Optional[str] = None
    tax_phylum: Optional[str] = None
    tax_class: Optional[str] = None
    tax_subclass: Optional[str] = None
    tax_order: Optional[str] = None
    tax_suborder: Optional[str] = None
    tax_superfamily: Optional[str] = None
    tax_family: Optional[str] = None
    tax_subfamily: Optional[str] = None
    tax_genus: Optional[str] = None
    tax_species: Optional[str] = None
    tax_subspecies: Optional[str] = None

class HARM_Species_to_Record(BaseModel):
    fk_species_identifier: Optional[UUID] = None
    fk_data_record: str