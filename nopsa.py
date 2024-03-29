from pydantic import BaseModel, Field, validator
from typing import Generic, List, Optional, TypeVar
from datetime import datetime
from fastapi import FastAPI
from enum import Enum
from uuid import UUID, uuid4

from maintenance import Maintenance, MaintenanceStatus, MaintenanceType
from bicycle import Bicycle
from bicyclegarage import BicycleGarage

app = FastAPI()


bikes = {
    0: Bicycle(
        name="Cube Exporer",
        description="Hihntavetoinen työmatkapyörä",
        frame_number="T334333",
        maintenance=[
            Maintenance(
                name="Ketjun kiristys",
                description="Ketju löysällä",
                maintenance_status=MaintenanceStatus.done,
                maintenance_type=MaintenanceType.service,
                price=10.0,
                done_at=datetime.now(),
            ),
            Maintenance(
                name="Uusi hihna",
                description="Hihna meni keuliessa poikki",
                maintenance_status=MaintenanceStatus.pending,
                maintenance_type=MaintenanceType.repair,
                price=100.0,
                done_at=None,
            ),
        ],
    ),
    1: Bicycle(
        name="Radon R1",
        description="Maantiepyörä",
    ),
    2: Bicycle(
        name="Rose Dr. Z",
        description="XC täysjousto",
    ),
    3: Bicycle(
        name="Rose The Tusker",
        description="Fatbike",
    ),
}

bike = Bicycle(name="Otto Kynast", description="Länsisaksalainen putkirunkopyörä")

garage = BicycleGarage(name="Alakerta", description="Fillarikellari", bicycles=bikes.values())
garage.addfillari(bike)

bike.addmaintenance(
    Maintenance(name="Ketjun kiristys", description="Ketju löysällä")
    .adddone()
    .addprice(30.0)
    .addtype(MaintenanceType.service)
)


@app.get("/")
async def read_root():
    return {"garage": garage}


@app.post("/fillari/")
async def create_fillari(fillari: Bicycle):
    if garage.addfillari(fillari) is None:
        return {"error": "Fillari on jo tallennettu"}
    return fillari


@app.get("/fillari/{fillari_id}")
async def read_fillari(fillari_id: UUID):
    for fillari in garage.bicycles:
        if fillari.id == fillari_id:
            return fillari
