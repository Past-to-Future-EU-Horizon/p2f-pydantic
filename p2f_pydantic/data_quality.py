from pydantic import BaseModel
from pydantic import EmailStr
from uuid import UUID

class dq_comment(BaseModel):
    email: EmailStr
    comment: str
    dataset_id: UUID

class dq_rating(BaseModel):
    email: EmailStr
    rating: int
    dataset_id: UUID