from datetime import date, datetime
from typing import List
from apps.adapters.BaseModel import BaseModel


class Schema_Category(BaseModel):
    record_id : int
    name : str
    
    class Config:
        orm_mode = True

class FastCategories(BaseModel):
    items: List[Schema_Category]
    
    @classmethod
    def from_qs(cls, qs):
        return cls(items=Schema_Category.from_orms(qs))