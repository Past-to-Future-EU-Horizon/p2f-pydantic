from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal

class Keywords(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    keyword: str
    taxon: Optional[str] = None


class KeywordDictionary(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    keyword: str
    taxon: Optional[str] = None
    usage: int = 0