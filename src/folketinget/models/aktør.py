from datetime import datetime
from pydantic import BaseModel


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
