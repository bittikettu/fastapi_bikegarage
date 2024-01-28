from pydantic import BaseModel, Field, validator
from typing import  Generic, List, Optional, TypeVar
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

class MaintenanceStatus(str, Enum):
    done = "done"
    pending = "pending"
    started = "started"

class MaintenanceType(str, Enum):
    repair = "repair"
    service = "service"
    warranty = "warranty"

class Maintenance(BaseModel):
    id: UUID = uuid4()
    name: str
    description: str
    maintenance_status: Optional[MaintenanceStatus] = MaintenanceStatus.pending
    maintenance_type: Optional[MaintenanceType] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    price: Optional[float] = None
    done_at: Optional[datetime] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def adddone(self):
        self.updated_at = datetime.now()
        self.done_at = datetime.now()
        self.maintenance_status = MaintenanceStatus.done
        return self
    
    def addprice(self, price: float):
        self.updated_at = datetime.now()
        self.price = price
        return self
    
    def addtype(self, maintenance_type: MaintenanceType):
        self.updated_at = datetime.now()
        self.maintenance_type = maintenance_type
        return self