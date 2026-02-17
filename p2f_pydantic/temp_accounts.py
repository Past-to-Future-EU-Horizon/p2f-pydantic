from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

class temp_accounts(BaseModel):
    email: EmailStr
    token: str
    expiration: datetime

class request_token(BaseModel):
    email: EmailStr