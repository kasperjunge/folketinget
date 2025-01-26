import httpx
import pytest
from folketinget.models import *

BASE_URL = "https://oda.ft.dk/api/"

models_and_endpoints = [
    (EntitetBeskrivelse, "EntitetBeskrivelse"),
    (KolloneBeskrivelse, "KolloneBeskrivelse"),
    (Sagstrinsstatus, "Sagstrinsstatus"),
    (Sagstrinstype, "Sagstrinstype"),
    (Sagstrin, "Sagstrin"),
    (Sagsstatus, "Sagsstatus"),
    (Sagskategori, "Sagskategori"),
    (Sagstype, "Sagstype"),
    (Sag, "Sag"),
    (Sag, "Aktstykke"),
    (Sag, "Almdel"),
    (Sag, "Debat"),
    (Sag, "Forslag"),
    (Emneord, "Emneord"),
    (Emneordstype, "Emneordstype"),
    (Periode, "Periode"),
    (SagAktør, "SagAktør"),
    (SagAktørRolle, "SagAktørRolle"),
    (SagDokumentRolle, "SagDokumentRolle"),
    (SagDokument, "SagDokument"),
    (SagstrinAktør, "SagstrinAktør"),
    (SagstrinAktørRolle, "SagstrinAktørRolle"),
    (SagstrinDokument, "SagstrinDokument"),
    (EmneordDokument, "EmneordDokument"),
    (EmneordSag, "EmneordSag"),
    (DokumentAktørRolle, "DokumentAktørRolle"),
    (DokumentAktør, "DokumentAktør"),
    (DagsordenspunktDokument, "DagsordenspunktDokument"),
    (DagsordenspunktSag, "DagsordenspunktSag"),
    (MødeAktør, "MødeAktør"),
    (AktørAktørRolle, "AktørAktørRolle"),
    (AktørAktør, "AktørAktør"),
    (Dokumentkategori, "Dokumentkategori"),
    (Dokumentstatus, "Dokumentstatus"),
    (Dokumenttype, "Dokumenttype"),
    (Dokument, "Dokument"),
    (Fil, "Fil"),
    (Omtryk, "Omtryk"),
    (Aktørtype, "Aktørtype"),
    (Aktør, "Aktør"),
    (Mødestatus, "Mødestatus"),
    (Mødetype, "Mødetype"),
    (Stemmetype, "Stemmetype"),
    (Afstemningstype, "Afstemningstype"),
    (Afstemning, "Afstemning"),
    (Stemme, "Stemme"),
    (Dagsordenspunkt, "Dagsordenspunkt"),
    (Møde, "Møde"),
    # Not working
    # (EUsag, "EUsag"),
    # (Sambehandlinger, "Sambehandlinger"),
    # Add additional models as needed...
]


@pytest.mark.parametrize("model_class, endpoint", models_and_endpoints)
def test_model_instantiation(model_class, endpoint: str):
    with httpx.Client() as client:

        url = f"{BASE_URL}{endpoint}?$top=1"
        response = client.get(url)
        response.raise_for_status()

        json_data = response.json()
        # OData responses typically include a "value" key with an array of records.
        records = json_data.get("value", [])
        assert records, f"No records found for endpoint {endpoint}"

        # Use the first record to instantiate the model.
        record = records[0]
        try:
            instance = model_class(**record, objecttype=endpoint.lower())
        except Exception as e:
            pytest.fail(f"Failed to instantiate {model_class.__name__} from data: {e}")

        assert isinstance(instance, model_class)
        # Additional field-specific assertions can be added here if needed.
