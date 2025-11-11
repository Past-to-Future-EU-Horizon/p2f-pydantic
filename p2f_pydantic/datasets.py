from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import UUID

class Datasets(BaseModel):
    dataset_identifier: Optional[UUID] = None
    doi: str
    title: str
    sub_dataset_name: Optional[str] = None
    publication_date: date
    is_new_p2f: bool = False
    is_sub_dataset: bool = False

    
## dataset_datacite not included here as it will be an API server side 
## collected resource only, and will be downloaded as a JSON or XML
## literal, not parsed into a proper table. This can change in the 
## future. 