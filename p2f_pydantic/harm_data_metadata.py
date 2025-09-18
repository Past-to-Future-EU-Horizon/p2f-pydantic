from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class harm_location(BaseModel):
    pk_harm_location: Optional[int] = None
    location_identifier: UUID
    location_name: Optional[str] = None
    location_code: Optional[str] = None
    latitude: float
    longitude: float
    elevation: float
    location_age: int

class harm_location_to_record(BaseModel):
    pk_harm_location_to_record: Optional[int] = None
    fk_harm_location: UUID
    fk_data_record: str

class harm_data_species(BaseModel):
    pk_harm_species: Optional[int] = None
    species_identifier: UUID
    display_species: str
    common_name: Optional[str] = None
    tax_kingdom: Optional[str] = None
    tax_phylum: Optional[str] = None
    tax_class: Optional[str] = None
    tax_order: Optional[str] = None
    tax_family: Optional[str] = None
    tax_genus: Optional[str] = None
    tax_species: Optional[str] = None

class harm_species_to_record(BaseModel):
    pk_harm_species_to_record: Optional[int] = None
    fk_species_identifier: UUID
    fk_data_record: str