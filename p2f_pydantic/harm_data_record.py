from pydantic import BaseModel
from typing import Optional

class harm_data_record(BaseModel):
    pk_harm_data_record: Optional[int]
    fk_dataset: int