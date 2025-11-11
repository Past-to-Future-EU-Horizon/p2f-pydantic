from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class harm_location(BaseModel):
    location_identifier: Optional[UUID] = None
    location_name: Optional[str] = None
    location_code: Optional[str] = None
    latitude: float
    longitude: float
    elevation: float
    location_age: int

class harm_location_to_record(BaseModel):
    fk_harm_location: UUID
    fk_data_record: str

class harm_bounding_box(BaseModel):
    north: float
    east: float
    south: float
    west: float

class harm_data_species(BaseModel):
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

class harm_species_to_record(BaseModel):
    fk_species_identifier: Optional[UUID] = None
    fk_data_record: str