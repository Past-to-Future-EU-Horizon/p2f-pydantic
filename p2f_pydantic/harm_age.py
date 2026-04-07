from pydantic import BaseModel

class HARM_Data_Age(BaseModel):
    fk_record_hash: str
    age_mean: int
    age_recent: int
    age_oldest: int