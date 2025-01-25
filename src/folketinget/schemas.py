from datetime import datetime
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
    folketingstidendeurl: str | None = None  # Nullable field
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
    afgørelse: str | None = None
    afgørelsesdato: datetime | None = None
    afgørelsesresultatkode: str | None = None
    afstemningskonklusion: str | None = None
    baggrundsmateriale: str | None = None
    begrundelse: str | None = None
    deltundersagid: int | None = None
    fremsatundersagid: int | None = None
    id: int
    kategoriid: int
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


class Aktstykke(BaseModel):
    afgørelse: str | None = None
    afgørelsesdato: datetime | None = None
    afgørelsesresultatkode: str | None = None
    afstemningskonklusion: str
    baggrundsmateriale: str | None = None
    begrundelse: str | None = None
    deltundersagid: int | None = None
    fremsatundersagid: int | None = None
    id: int
    kategoriid: int
    lovnummer: str
    lovnummerdato: datetime | None = None
    nummer: str
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


class Almdel(BaseModel):
    afgørelse: str | None = None
    afgørelsesdato: datetime | None = None
    afgørelsesresultatkode: str | None = None
    afstemningskonklusion: str | None = None
    baggrundsmateriale: str | None = None
    begrundelse: str | None = None
    deltundersagid: int | None = None
    fremsatundersagid: int | None = None
    id: int
    kategoriid: int | None = None
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


class Debat(BaseModel):
    afgørelse: str | None = None
    afgørelsesdato: datetime | None = None
    afgørelsesresultatkode: str | None = None
    afstemningskonklusion: str | None = None
    baggrundsmateriale: str | None = None
    begrundelse: str | None = None
    deltundersagid: int | None = None
    fremsatundersagid: int | None = None
    id: int
    kategoriid: int | None = None
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


class Forslag(BaseModel):
    afgørelse: str | None = None
    afgørelsesdato: datetime | None = None
    afgørelsesresultatkode: str | None = None
    afstemningskonklusion: str | None = None
    baggrundsmateriale: str | None = None
    begrundelse: str | None = None
    deltundersagid: int | None = None
    fremsatundersagid: int | None = None
    id: int
    kategoriid: int | None = None
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


# Aktør
class Aktørtype(BaseModel):
    id: int
    opdateringsdato: datetime
    type: str


class Aktør(BaseModel):
    biografi: str | None = None
    efternavn: str | None = None
    fornavn: str | None = None
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
