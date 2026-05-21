from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

class HARM_Data_Record(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fk_dataset: UUID
    record_hash: str
