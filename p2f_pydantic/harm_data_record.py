from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class harm_data_record(BaseModel):
    fk_dataset: UUID
    record_hash: str
