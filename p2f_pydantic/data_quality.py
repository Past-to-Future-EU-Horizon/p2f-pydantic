from pydantic import BaseModel
from pydantic import EmailStr
from uuid import UUID
from typing import Optional

class DQ_Comment(BaseModel):
    comment_id: Optional[UUID]=None
    email: EmailStr
    comment: str
    dataset_id: UUID

class DQ_Rating(BaseModel):
    email: EmailStr
    rating: int
    dataset_id: UUID