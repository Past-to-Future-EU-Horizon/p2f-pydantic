from pydantic import BaseModel, ConfigDict
from typing import Literal
from uuid import UUID

class Core(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    core_id: UUID | None = None
    core_name: str
    core_notes: str | None = None
    core_type: Literal["ice", "sediment", "other"] = "other"
    total_length: float | None = None
    fk_location: UUID | None = None

class CoreSegment(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fk_core_id: UUID
    segment_name: str
    segment_notes: str | None = None
    core_segment_id: UUID | None = None
    segment_center: float | None = None
    segment_start: float | None = None
    segment_end: float | None = None