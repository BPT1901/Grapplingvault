from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JournalEntry(BaseModel):
    title: str
    category: str
    entry: str
    date: Optional[datetime] = datetime.now()