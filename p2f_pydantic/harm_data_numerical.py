from pydantic import BaseModel
from typing import Optional, Literal, Union, List
from uuid import UUID

class HARM_Int_Confidence(BaseModel):
    value: int
    upper_conf_interval: float
    lower_conf_interval: float
    upper_conf_value: int
    lower_conf_value: int
    fk_data_record: str
    fk_data_type: UUID

class HARM_Int(BaseModel):
    value: int
    fk_data_record: str
    fk_data_type: UUID

class HARM_Float_Confidence(BaseModel):
    value: float
    upper_conf_interval: float
    lower_conf_interval: float
    upper_conf_value: float
    lower_conf_value: float
    fk_data_record: str
    fk_data_type: UUID

class HARM_Float(BaseModel):
    value: float
    fk_data_record: str
    fk_data_type: UUID

class Insert_HARM_Numerical(BaseModel):
    fk_data_record: str
    fk_data_type: UUID
    numerical_type: Literal["INT", "FLOAT"]
    value: Union[int, float]
    upper_conf_interval: Optional[Union[int, float]] = None
    lower_conf_interval: Optional[Union[int, float]] = None
    upper_conf_value: Optional[Union[int, float]] = None
    lower_conf_value: Optional[Union[int, float]] = None

class Return_HARM_Numerical(BaseModel):
    data_harmonized_int: Optional[List[HARM_Int]] = None
    data_harmonized_int_confidence: Optional[List[HARM_Int_Confidence]] = None
    data_harmonized_float: Optional[List[HARM_Float]] = None
    data_harmonized_float_confidence: Optional[List[HARM_Float_Confidence]] = None