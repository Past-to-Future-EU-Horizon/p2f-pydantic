from pydantic import BaseModel
from typing import Optional, Literal
from uuid import UUID

class Seasonality_DS(BaseModel):
    seasonality_type: Literal["Winter/Summer", 
                              "Spring/Summer/Fall/Winter", 
                              "Hot/Cold", 
                              "None"]
    
class Season(BaseModel):
    season: Literal["Summer", 
                    "Spring", 
                    "Fall",
                    "Winter", 
                    "Hot", 
                    "Cold",
                    "None"]