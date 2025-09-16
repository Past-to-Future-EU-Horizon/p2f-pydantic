from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class harm_data_record(BaseModel):
    pk_harm_data_record: Optional[int] = None
    fk_dataset: UUID
    record_hash: str
