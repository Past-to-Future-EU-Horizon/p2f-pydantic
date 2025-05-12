from pydantic import BaseModel
from datetime import date
from typing import Optional

class Datasets(BaseModel):
    pk_datasets: Optional[int]
    doi: str
    title: str
    publication_date: date