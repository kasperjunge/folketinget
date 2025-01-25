from datetime import datetime
from pydantic import BaseModel


class Mødestatus(BaseModel):
    id: int
    opdateringsdato: datetime
    status: str


class Mødetype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str


class Stemmetype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str


class Afstemningstype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str


class Afstemning(BaseModel):
    id: int
    kommentar: str | None = None
    konklusion: str
    mødeid: int
    nummer: int
    opdateringsdato: datetime
    sagstrinid: int | None = None
    typeid: int
    vedtaget: bool


class Stemme(BaseModel):
    afstemningid: int
    aktørid: int
    id: int
    opdateringsdato: datetime
    typeid: int


class Dagsordenspunkt(BaseModel):
    forhandling: str | None = None
    forhandlingskode: str
    id: int
    kommentar: str
    kørebemærkning: str | None = None
    mødeid: int
    nummer: str
    offentlighedskode: str
    opdateringsdato: datetime
    sagstrinid: int | None = None
    superid: int | None = None
    titel: str


class Møde(BaseModel):
    dagsordenurl: str
    dato: datetime
    id: int
    lokale: str
    nummer: str | None = None
    offentlighedskode: str
    opdateringsdato: datetime
    periodeid: int
    starttidsbemærkning: str
    statusid: int
    titel: str
    typeid: int
