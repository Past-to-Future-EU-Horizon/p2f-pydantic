from pydantic import BaseModel
from typing import Optional

class semantic_version(BaseModel):
    major: int
    minor: int
    patch: int

class api_metadata(BaseModel):
    pyclient_minimum_version: Optional[semantic_version]
    api_system_version: Optional[semantic_version]