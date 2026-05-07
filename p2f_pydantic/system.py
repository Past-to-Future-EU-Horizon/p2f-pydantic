from pydantic import BaseModel
from typing import Optional, Literal

class Semantic_Version(BaseModel):
    major: int
    minor: int
    patch: int

class API_Metadata(BaseModel):
    pyclient_minimum_version: Optional[Semantic_Version] = None
    api_system_version: Optional[Semantic_Version] = None
    record_hash_algorithm: Optional[Literal["MD5", "SHA256", "SHA384", "SHA512"]]="MD5" # MD5 future default
