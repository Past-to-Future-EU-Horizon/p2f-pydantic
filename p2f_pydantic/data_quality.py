from pydantic import BaseModel
from pydantic import EmailStr
from uuid import UUID
from typing import Optional

class dq_comment(BaseModel):
    comment_id: Optional[UUID]=None
    email: EmailStr
    comment: str
    dataset_id: UUID

class dq_rating(BaseModel):
    email: EmailStr
    rating: int
    dataset_id: UUID