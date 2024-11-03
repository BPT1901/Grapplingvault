from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JournalEntrySchema(BaseModel):
    title: str
    category: str
    entry: str
    date: datetime
    _id: Optional[str] = None