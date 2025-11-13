from pydantic import BaseModel
from pydantic import HttpUrl
from typing import Optional
from uuid import UUID

class harm_reference(BaseModel):
    reference_id: Optional[UUID] = None
    doi: Optional[HttpUrl] = None
    other_link: Optional[HttpUrl] = None
    reference_type: Optional[str] = None
    reference_content: Optional[str] = None