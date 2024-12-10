from typing import List
from pydantic import BaseModel

class NameOccurrence(BaseModel):
    name: str
    count: int

class NamesOccurrencesResponse(BaseModel):
    names: List[NameOccurrence]