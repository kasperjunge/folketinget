from datetime import datetime
from pydantic import BaseModel


class Sagstrinsstatus(BaseModel):
    id: int
    opdateringsdato: datetime
    status: str


class Sagstrinstype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str


class Sagstrin(BaseModel):
    dato: datetime
    folketingstidende: str
    folketingstidendesidenummer: str
    folketingstidendeurl: str | None = None  # Nullable field
    id: int
    opdateringsdato: datetime
    sagid: int
    statusid: int
    titel: str
    typeid: int
