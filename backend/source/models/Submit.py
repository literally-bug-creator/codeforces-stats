from pydantic import BaseModel
from datetime import date
from typing import Optional

class Submit(BaseModel):
    problemset_name: str
    verdict: str
    time: date
    tags: list
    rating: Optional[int]