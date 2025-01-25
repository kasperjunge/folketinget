from datetime import datetime
from pydantic import BaseModel


class Dokumentkategori(BaseModel):
    id: int
    kategori: str
    opdateringsdato: datetime


class Dokumentstatus(BaseModel):
    id: int
    status: str
    opdateringsdato: datetime


class Dokumenttype(BaseModel):
    id: int
    type: str
    opdateringsdato: datetime


class Dokument(BaseModel):
    dagsordenudgavenummer: int | None = None
    dato: datetime
    frigivelsesdato: datetime
    grundnotatstatus: str
    id: int
    kategoriid: int
    modtagelsesdato: datetime | None = None
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: str
    paragrafnummer: str
    procedurenummer: str
    spørgsmaalsid: int | None = None
    spørgsmaalsordlyd: str | None = None
    spørgsmaalstitel: str | None = None
    statusid: int
    titel: str
    typeid: int


class Fil(BaseModel):
    dokumentid: int
    filurl: str
    format: str
    id: int
    opdateringsdato: datetime
    titel: str
    variantkode: str
    versionsdato: datetime


class Omtryk(BaseModel):
    begrundelse: str
    dato: datetime
    dokumentid: int
    id: int
    opdateringsdato: datetime
