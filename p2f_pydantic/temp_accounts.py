from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime
from typing import Optional

class Temp_Account(BaseModel):
    email: EmailStr
    token: Optional[str] = None
    expiration: Optional[datetime] = None