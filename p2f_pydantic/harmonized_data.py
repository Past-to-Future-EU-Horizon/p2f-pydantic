from pydantic import BaseModel
from typing import Optional

class harmonized_int_confidence(BaseModel):
    pk_harm_int_conf: Optional[int]
    value: int
    upper_conf_interval: float
    lower_conf_interval: float
    upper_conf_value: int
    lower_conf_value: int
    data_record: int

class harmonized_int(BaseModel):
    pk_harm_int: Optional[int]
    value: int
    data_record: int

class harmonized_float_confidence(BaseModel):
    pk_harm_float_conf: Optional[int]
    value: float
    upper_conf_interval: float
    lower_conf_interval: float
    upper_conf_value: float
    lower_conf_value: float
    data_record: int
    
class harmonized_float_confidence(BaseModel):
    pk_harm_float: Optional[int]
    value: float
    data_record: int
    