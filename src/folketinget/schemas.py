from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Øvrige
class EntitetBeskrivelse(BaseModel):
    beskrivelse: str
    entitetnavn: str
    id: int
    opdateringsdato: datetime


class KolloneBeskrivelse(BaseModel):
    beskrivelse: str
    entitetnavn: str
    id: int
    kollonenavn: str
    opdateringsdato: datetime


# Sagstrin
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
    folketingstidendeurl: Optional[str] = None  # Nullable field
    id: int
    opdateringsdato: datetime
    sagid: int
    statusid: int
    titel: str
    typeid: int


# Sag
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
    afgørelse: Optional[str] = None
    afgørelsesdato: Optional[datetime] = None
    afgørelsesresultatkode: Optional[str] = None
    afstemningskonklusion: Optional[str] = None
    baggrundsmateriale: Optional[str] = None
    begrundelse: Optional[str] = None
    deltundersagid: Optional[int] = None
    fremsatundersagid: Optional[int] = None
    id: int
    kategoriid: int
    lovnummer: Optional[str] = None
    lovnummerdato: Optional[datetime] = None
    nummer: Optional[str] = None
    nummernumerisk: str
    nummerpostfix: str
    nummerprefix: str
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: Optional[str] = None
    paragrafnummer: Optional[int] = None
    periodeid: int
    resume: str
    retsinformationsurl: Optional[str] = None
    rådsmødedato: Optional[datetime] = None
    statsbudgetsag: bool
    statusid: int
    titel: str
    titelkort: str
    typeid: int


class Aktstykke(BaseModel):
    afgørelse: Optional[str] = None
    afgørelsesdato: Optional[datetime] = None
    afgørelsesresultatkode: Optional[str] = None
    afstemningskonklusion: str
    baggrundsmateriale: Optional[str] = None
    begrundelse: Optional[str] = None
    deltundersagid: Optional[int] = None
    fremsatundersagid: Optional[int] = None
    id: int
    kategoriid: int
    lovnummer: str
    lovnummerdato: Optional[datetime] = None
    nummer: str
    nummernumerisk: str
    nummerpostfix: str
    nummerprefix: str
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: Optional[str] = None
    paragrafnummer: Optional[int] = None
    periodeid: int
    resume: str
    retsinformationsurl: Optional[str] = None
    rådsmødedato: Optional[datetime] = None
    statsbudgetsag: bool
    statusid: int
    titel: str
    titelkort: str
    typeid: int


class Almdel(BaseModel):
    afgørelse: Optional[str] = None
    afgørelsesdato: Optional[datetime] = None
    afgørelsesresultatkode: Optional[str] = None
    afstemningskonklusion: Optional[str] = None
    baggrundsmateriale: Optional[str] = None
    begrundelse: Optional[str] = None
    deltundersagid: Optional[int] = None
    fremsatundersagid: Optional[int] = None
    id: int
    kategoriid: Optional[int] = None
    lovnummer: Optional[str] = None
    lovnummerdato: Optional[datetime] = None
    nummer: Optional[str] = None
    nummernumerisk: str
    nummerpostfix: str
    nummerprefix: str
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: Optional[str] = None
    paragrafnummer: Optional[int] = None
    periodeid: int
    resume: str
    retsinformationsurl: Optional[str] = None
    rådsmødedato: Optional[datetime] = None
    statsbudgetsag: bool
    statusid: int
    titel: str
    titelkort: str
    typeid: int


class Debat(BaseModel):
    afgørelse: Optional[str] = None
    afgørelsesdato: Optional[datetime] = None
    afgørelsesresultatkode: Optional[str] = None
    afstemningskonklusion: Optional[str] = None
    baggrundsmateriale: Optional[str] = None
    begrundelse: Optional[str] = None
    deltundersagid: Optional[int] = None
    fremsatundersagid: Optional[int] = None
    id: int
    kategoriid: Optional[int] = None
    lovnummer: Optional[str] = None
    lovnummerdato: Optional[datetime] = None
    nummer: Optional[str] = None
    nummernumerisk: str
    nummerpostfix: str
    nummerprefix: str
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: Optional[str] = None
    paragrafnummer: Optional[int] = None
    periodeid: int
    resume: str
    retsinformationsurl: Optional[str] = None
    rådsmødedato: Optional[datetime] = None
    statsbudgetsag: bool
    statusid: int
    titel: str
    titelkort: str
    typeid: int


class Forslag(BaseModel):
    afgørelse: Optional[str] = None
    afgørelsesdato: Optional[datetime] = None
    afgørelsesresultatkode: Optional[str] = None
    afstemningskonklusion: Optional[str] = None
    baggrundsmateriale: Optional[str] = None
    begrundelse: Optional[str] = None
    deltundersagid: Optional[int] = None
    fremsatundersagid: Optional[int] = None
    id: int
    kategoriid: Optional[int] = None
    lovnummer: Optional[str] = None
    lovnummerdato: Optional[datetime] = None
    nummer: Optional[str] = None
    nummernumerisk: str
    nummerpostfix: str
    nummerprefix: str
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: Optional[str] = None
    paragrafnummer: Optional[int] = None
    periodeid: int
    resume: str
    retsinformationsurl: Optional[str] = None
    rådsmødedato: Optional[datetime] = None
    statsbudgetsag: bool
    statusid: int
    titel: str
    titelkort: str
    typeid: int


class EUsag(BaseModel):
    afgørelse: str
    afgørelsesdato: datetime
    afgørelsesresultatkode: str
    afstemningskonklusion: str
    baggrundsmateriale: str
    begrundelse: str
    deltundersagid: int
    fremsatundersagid: int
    id: int
    kategoriid: int
    lovnummer: str
    lovnummerdato: datetime
    nummer: str
    nummernumerisk: str
    nummerpostfix: str
    nummerprefix: str
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: str
    paragrafnummer: int
    periodeid: int
    resume: str
    retsinformationsurl: str
    rådsmødedato: datetime
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


# Relationer
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
    rolleid: Optional[int] = None  # Made optional to handle missing or mismatched field
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
    slutdato: Optional[datetime] = None
    startdato: datetime
    tilaktørid: int


# Dokument
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
    dagsordenudgavenummer: Optional[int] = None
    dato: datetime
    frigivelsesdato: datetime
    grundnotatstatus: str
    id: int
    kategoriid: int
    modtagelsesdato: Optional[datetime] = None
    offentlighedskode: str
    opdateringsdato: datetime
    paragraf: str
    paragrafnummer: str
    procedurenummer: str
    spørgsmaalsid: Optional[int] = None
    spørgsmaalsordlyd: Optional[str] = None
    spørgsmaalstitel: Optional[str] = None
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


# Aktør
class Aktørtype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str


class Aktør(BaseModel):
    biografi: Optional[str] = None
    efternavn: Optional[str] = None
    fornavn: Optional[str] = None
    gruppenavnkort: str
    id: int
    navn: str
    opdateringsdato: datetime
    periodeid: int
    slutdato: datetime
    startdato: datetime
    typeid: int


# Møde
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
    kommentar: Optional[str] = None
    konklusion: str
    mødeid: int
    nummer: int
    opdateringsdato: datetime
    sagstrinid: Optional[int] = None
    typeid: int
    vedtaget: bool


class Stemme(BaseModel):
    afstemningid: int
    aktørid: int
    id: int
    opdateringsdato: datetime
    typeid: int


class Dagsordenspunkt(BaseModel):
    forhandling: Optional[str] = None
    forhandlingskode: str
    id: int
    kommentar: str
    kørebemærkning: Optional[str] = None
    mødeid: int
    nummer: str
    offentlighedskode: str
    opdateringsdato: datetime
    sagstrinid: Optional[int] = None
    superid: Optional[int] = None
    titel: str


class Møde(BaseModel):
    dagsordenurl: str
    dato: datetime
    id: int
    lokale: str
    nummer: Optional[str] = None
    offentlighedskode: str
    opdateringsdato: datetime
    periodeid: int
    starttidsbemærkning: str
    statusid: int
    titel: str
    typeid: int
