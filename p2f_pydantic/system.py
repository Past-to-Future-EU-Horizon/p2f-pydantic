from pydantic import BaseModel
from typing import Optional

class Semantic_Version(BaseModel):
    major: int
    minor: int
    patch: int

class API_Metadata(BaseModel):
    pyclient_minimum_version: Optional[Semantic_Version] = None
    api_system_version: Optional[Semantic_Version] = None