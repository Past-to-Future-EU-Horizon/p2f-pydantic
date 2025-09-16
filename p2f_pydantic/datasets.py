from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import UUID

class Datasets(BaseModel):
    pk_datasets: Optional[int]
    dataset_identifier: UUID
    doi: str
    title: str
    publication_date: date
    is_new_p2f: bool

## dataset_datacite not included here as it will be an API server side 
## collected resource only, and will be downloaded as a JSON or XML
## literal, not parsed into a proper table. This can change in the 
## future. 