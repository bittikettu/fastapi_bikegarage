from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4
from maintenance import Maintenance


class Bicycle(BaseModel):
    id: UUID = uuid4()
    frame_number: Optional[str] = None
    name: str
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    sold_at: Optional[datetime] = None
    maintenance: Optional[List[Maintenance]] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def addmaintenance(self, maintenance: Maintenance):
        if self.maintenance is None:
            self.maintenance = []
        self.updated_at = datetime.now()
        self.maintenance.append(maintenance)

    def __eq__(self, other):
        if isinstance(other, Bicycle):
            return self.name == other.name and self.description == other.description and self.frame_number == other.frame_number
