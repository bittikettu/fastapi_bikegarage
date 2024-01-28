from pydantic import BaseModel, Field, validator
from typing import  Generic, List, Optional, TypeVar
from datetime import datetime
from fastapi import FastAPI
from enum import Enum

class MaintenanceStatus(str, Enum):
    done = "done"
    pending = "pending"
    started = "started"

class MaintenanceType(str, Enum):
    repair = "repair"
    service = "service"
    warranty = "warranty"

app = FastAPI()

class Maintenance(BaseModel):
    id: int
    name: str
    description: str
    maintenance_status: Optional[MaintenanceStatus] = None
    maintenance_type: Optional[MaintenanceType] = None
    created_at: datetime
    updated_at: datetime
    price: float
    done_at: Optional[datetime] = None

class Fillari(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    sold_at: Optional[datetime] = None
    maintenance: Optional[List[Maintenance]] = None

    def addmaintenance(self, maintenance: Maintenance):
        if self.maintenance is None:
            self.maintenance = []
        self.updated_at = datetime.now()
        self.maintenance.append(maintenance)

class Fillarikellari(BaseModel):
    id: int
    name: str
    description: str
    fillarit: List[Fillari] = []

    def addfillari(self, fillari: Fillari):
        if self.fillarit is None:
            self.fillarit = []
        self.fillarit.append(fillari)

filot = {
    0: Fillari(
        id=0,
        name="Cube Exporer",
        description="Hihntavetoinen työmatkapyörä",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        sold_at=None,
        maintenance=[
            Maintenance(
                id=0,
                name="Ketjun kiristys",
                description="Ketju löysällä",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                maintenance_status=MaintenanceStatus.done,
                maintenance_type=MaintenanceType.service,
                price=0.0,
                done_at=None,
            ),
            Maintenance(
                id=1,
                name="Uusi hihna",
                description="Hihna meni keuliessa poikki",
                created_at=datetime.now(),
                updated_at=datetime.now(),
                maintenance_status=MaintenanceStatus.pending,
                maintenance_type=MaintenanceType.repair,
                price=100.0,
                done_at=None,
            ),
        ]
    ),
    1: Fillari(
        id=1,
        name="Radon R1",
        description="Maantiepyörä",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        sold_at=None,
    ),
    2: Fillari(
        id=2,
        name="Rose Dr. Z",
        description="XC täysjousto",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        sold_at=None,
    ),
    3: Fillari(
        id=3,
        name="Rose The Tusker",
        description="Fatbike",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        sold_at=None,
    ),
}

warehouse = Fillarikellari(id=1, name="Alakerta", description="Fillarikellari", fillarit=filot.values())

@app.get("/")
async def read_root():
    return {"varasto": warehouse}

@app.post("/fillari/")
async def create_fillari(fillari: Fillari):
    warehouse.addfillari(fillari)
    return fillari

@app.get("/fillari/{fillari_id}")
async def read_fillari(fillari_id: int):
    return warehouse.fillarit[fillari_id]