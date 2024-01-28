from pydantic import BaseModel, Field, validator
from typing import Generic, List, Optional, TypeVar
from datetime import datetime
from fastapi import FastAPI
from enum import Enum
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
        self.bicycles.append(bicycle)
