from pydantic import BaseModel
from pydantic import HttpUrl
from typing import Optional
from uuid import UUID

class HARM_Reference(BaseModel):
    reference_id: Optional[UUID] = None
    # Now a string because storing the 10prefix/suffix is probably better
    doi: Optional[str] = None               
    other_link: Optional[HttpUrl] = None
    reference_type: Optional[str] = None
    reference_content: Optional[str] = None