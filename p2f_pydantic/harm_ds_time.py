from pydantic import BaseModel
from typing import Optional, Literal
from uuid import UUID

class HARM_DS_TimeCoverage(BaseModel):
    dataset_id: UUID
    oldest: int
    youngest: int
    reference_zero: int
    oldest_older_conf: Optional[int] = None
    oldest_younger_conf: Optional[int] = None
    youngest_older_conf: Optional[int] = None
    youngest_younger_conf: Optional[int] = None
    older_conf_interval: Optional[float] = None
    younger_conf_interval: Optional[float] = None

class HARM_DS_Seasonailty(BaseModel):
    dataset_id: UUID
    has_seasonality: bool
    seasonality_type: Optional[Literal["Hot/Cold", "Summer/Winter", "Spring/Summer/Winter/Fall", "Other"]] = None

class HARM_DS_Frequency(BaseModel):
    dataset_id: UUID
    mean_frequency: Optional[int]
    shortest_frequency: Optional[int]
    longest_frequency: Optional[int]