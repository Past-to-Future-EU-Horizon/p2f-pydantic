from pydantic import BaseModel
from typing import Optional, Literal
from uuid import UUID

class Age_Model(BaseModel):
    age_model_id: Optional[UUID] = None
    model_name: str
    model_description: Optional[str] = None