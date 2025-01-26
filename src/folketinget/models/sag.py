from datetime import datetime
from pydantic import BaseModel, Field
from enum import StrEnum, auto


class ObjectType(StrEnum):
    AKTSTYKKE = auto()
    ALMDEL = auto()
    DEBAT = auto()
    FORSLAG = auto()
    SAG = auto()
    EUSAG = auto()


class Sagsstatus(BaseModel):
    id: int
    opdateringsdato: datetime
    status: str


class Sagskategori(BaseModel):
    id: int
    kategori: str
    opdateringsdato: datetime


class Sagstype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str


class Sag(BaseModel):
    objecttype: ObjectType = Field(description="Type of object")
    afgørelse: str | None = None
    afgørelsesdato: datetime | None = None
    afgørelsesresultatkode: str | None = None
    afstemningskonklusion: str | None = None
    baggrundsmateriale: str | None = None
    begrundelse: str | None = None
    deltundersagid: int | None = None
    fremsatundersagid: int | None = None
    id: int
    kategoriid: int | None
    lovnummer: str | None = None
    lovnummerdato: datetime | None = None
    nummer: str | None = None
    nummernumerisk: str
    nummerpostfix: str
    nummerprefix: str
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: str | None = None
    paragrafnummer: int | None = None
    periodeid: int
    resume: str
    retsinformationsurl: str | None = None
    rådsmødedato: datetime | None = None
    statsbudgetsag: bool
    statusid: int
    titel: str
    titelkort: str
    typeid: int


class Sambehandlinger(BaseModel):
    andetsagstrinid: int
    førstesagstrinid: int
    id: int
    opdateringsdato: datetime


class Emneord(BaseModel):
    emneord: str
    id: int
    opdateringsdato: datetime
    typeid: int


class Emneordstype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str
