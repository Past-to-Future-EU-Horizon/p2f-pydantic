from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class HARM_Data_Record(BaseModel):
    fk_dataset: UUID
    record_hash: str
