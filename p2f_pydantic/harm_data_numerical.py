from pydantic import BaseModel
from typing import Optional, Literal, Union
from uuid import UUID

class harmonized_int_confidence(BaseModel):
    pk_harm_num: Optional[UUID] = None
    value: int
    upper_conf_interval: float
    lower_conf_interval: float
    upper_conf_value: int
    lower_conf_value: int
    fk_data_record: str
    fk_data_type: int

class harmonized_int(BaseModel):
    pk_harm_num: Optional[UUID] = None
    value: int
    fk_data_record: str
    fk_data_type: int

class harmonized_float_confidence(BaseModel):
    pk_harm_num: Optional[UUID] = None
    value: float
    upper_conf_interval: float
    lower_conf_interval: float
    upper_conf_value: float
    lower_conf_value: float
    fk_data_record: str
    fk_data_type: int
    
class harmonized_float(BaseModel):
    pk_harm_num: Optional[UUID] = None
    value: float
    fk_data_record: str
    fk_data_type: int
    
## With this model below we can reduce the number of services needed
## to insert or update data in the database. 
## We just need to have a declaration of int or float, and if the 
## confidence values exist, we can further deduce the target table. 
class insert_harm_numerical(BaseModel):
    fk_data_record: str
    fk_data_type: int 
    numerical_type: Literal["INT", "FLOAT"]
    value: Union[int, float]
    upper_conf_interval: Optional[Union[int, float]] = None
    lower_conf_interval: Optional[Union[int, float]] = None
    upper_conf_value: Optional[Union[int, float]] = None
    lower_conf_value: Optional[Union[int, float]] = None