from datetime import datetime
from pydantic import BaseModel


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
