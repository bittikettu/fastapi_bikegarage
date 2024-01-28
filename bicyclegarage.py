from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4
from bicycle import Bicycle

class BicycleGarage(BaseModel):
    id: UUID = uuid4()
    name: str
    description: str
    bicycles: List[Bicycle] = []

    def addfillari(self, bicycle: Bicycle):
        if self.bicycles is None:
            self.bicycles = []
        if bicycle not in self.bicycles:
            self.bicycles.append(bicycle)
            return bicycle
        else:  
            return None
