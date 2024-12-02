from pydantic import BaseModel
from datetime import date
from typing import Optional

class Submit(BaseModel):
    time: date
    tags: list
    rating: Optional[int]

