from pydantic import BaseModel
from pydantic import AnyUrl
from datetime import date
from typing import Optional
from uuid import UUID

class Git_Repository(BaseModel):
    git_repo_id: Optional[UUID] = None
    git_repo_url: AnyUrl
    is_p2f_repo: bool = False