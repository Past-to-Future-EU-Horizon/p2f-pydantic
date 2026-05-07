from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class HARM_Species(BaseModel):
    species_id: Optional[UUID] = None
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
