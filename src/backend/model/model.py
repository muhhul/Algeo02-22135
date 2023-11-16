from typing import Optional
from pydantic import BaseModel
from enum import Enum


class dataTekstur(BaseModel):
    contrast:float
    homogency:float
    entropy:float
    filepath:str

class Tipe(str,Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "INCOME"
    PURCHASE = "PURCHASE"
    INVEST = "INVEST"

class inputTransaction(BaseModel):
    tipe:Tipe
    amount:int
    method:Optional[str]