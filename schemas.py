from datetime import datetime, date
from typing import List, Optional

from pydantic import BaseModel


class Driver(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    driving_score: float
    age: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DriverResponse(BaseModel):
    code: str
    msg: str
    records: List[Driver]


class DriverFilter(BaseModel):
    limit: int
    offset: int
    start_date: Optional[date]
    end_date: Optional[date]
    min_score: Optional[float]
    max_score: Optional[float]
