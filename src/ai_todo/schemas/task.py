from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    priority: int
    due_date: Optional[datetime] = None
    completed: bool = False

    class Config:
        orm_mode = True