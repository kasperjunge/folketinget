from datetime import datetime
from pydantic import BaseModel


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
