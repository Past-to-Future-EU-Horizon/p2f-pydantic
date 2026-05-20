from pydantic import BaseModel
from typing import Optional, Literal

class Keywords(BaseModel):
    keyword: str
    taxon: Optional[str] = None