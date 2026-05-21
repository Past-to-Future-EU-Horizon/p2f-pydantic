from pydantic import BaseModel, ConfigDict
from pydantic import EmailStr
from uuid import UUID
from typing import Optional

class DQ_Comment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    comment_id: Optional[UUID]=None
    email: EmailStr
    comment: str
    dataset_id: UUID

class DQ_Rating(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr
    rating: int
    dataset_id: UUID