from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class HARM_DS_TimeCoverage(BaseModel):
    dataset_id: UUID
    oldest: int
    youngest: int
    reference_zero: int
    oldest_older_conf = Optional[int] = None
    oldest_younger_conf = Optional[int] = None
    youngest_older_conf = Optional[int] = None
    youngest_younger_conf = Optional[int] = None
    older_conf_interval = Optional[float] = None
    younger_conf_interval = Optional[float] = None