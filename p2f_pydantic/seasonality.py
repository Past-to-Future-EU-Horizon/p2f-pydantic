from pydantic import BaseModel, ConfigDict
from typing import Optional, Literal
from uuid import UUID

class Seasonality_DS(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    dataset_id: UUID
    seasonality_type: Literal["Winter/Summer", 
                              "Spring/Summer/Fall/Winter", 
                              "Hot/Cold", 
                              "None"]
    
    
class Season(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    record_hash: str
    season: Literal["Summer", 
                    "Spring", 
                    "Fall",
                    "Winter", 
                    "Hot", 
                    "Cold",
                    "None"]