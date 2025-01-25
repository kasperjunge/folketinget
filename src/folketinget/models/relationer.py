from datetime import datetime
from pydantic import BaseModel


class Periode(BaseModel):
    id: int
    kode: str
    opdateringsdato: datetime
    slutdato: datetime
    startdato: datetime
    titel: str
    type: str


class SagAktør(BaseModel):
    aktørid: int
    id: int
    opdateringsdato: datetime
    rolleid: int
    sagid: int


class SagAktørRolle(BaseModel):
    id: int
    opdateringsdato: datetime
    rolle: str


class SagDokumentRolle(BaseModel):
    id: int
    opdateringsdato: datetime
    rolle: str


class SagDokument(BaseModel):
    bilagsnummer: str
    dokumentid: int
    frigivelsesdato: datetime
    id: int
    opdateringsdato: datetime
    rolleid: int | None = None  # Made optional to handle missing or mismatched field
    sagid: int


class SagstrinAktør(BaseModel):
    aktørid: int
    id: int
    opdateringsdato: datetime
    rolleid: int
    sagstrinid: int


class SagstrinAktørRolle(BaseModel):
    id: int
    opdateringsdato: datetime
    rolle: str


class SagstrinDokument(BaseModel):
    dokumentid: int
    id: int
    opdateringsdato: datetime
    sagstrinid: int


class EmneordDokument(BaseModel):
    dokumentid: int
    emneordid: int
    id: int
    opdateringsdato: datetime


class EmneordSag(BaseModel):
    emneordid: int
    id: int
    opdateringsdato: datetime
    sagid: int


class DokumentAktørRolle(BaseModel):
    id: int
    opdateringsdato: datetime
    rolle: str


class DokumentAktør(BaseModel):
    aktørid: int
    dokumentid: int
    id: int
    opdateringsdato: datetime
    rolleid: int


class DagsordenspunktDokument(BaseModel):
    dagsordenspunktid: int
    dokumentid: int
    id: int
    note: str
    opdateringsdato: datetime


class DagsordenspunktSag(BaseModel):
    dagsordenspunktid: int
    id: int
    opdateringsdato: datetime
    sagid: int


class MødeAktør(BaseModel):
    aktørid: int
    id: int
    mødeid: int
    opdateringsdato: datetime


class AktørAktørRolle(BaseModel):
    id: int
    opdateringsdato: datetime
    rolle: str


class AktørAktør(BaseModel):
    fraaktørid: int
    id: int
    opdateringsdato: datetime
    rolleid: int
    slutdato: datetime | None = None
    startdato: datetime
    tilaktørid: int
