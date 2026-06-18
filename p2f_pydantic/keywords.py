from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from uuid import UUID

class Keywords(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    keyword: str

class TaxonomicDict(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    taxdict_id: UUID
    keyword: str
    taxonomy: str
    parent_keyword: Optional[str] = None
    taxonomic_id: Optional[str] = None