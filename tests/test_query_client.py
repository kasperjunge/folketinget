import pytest
from datetime import datetime
import httpx

# Import the classes under test.
from folketinget.client.query_client import SagQueryClient

# ---------------------------------------------------------------------------
# Dummy response and dummy HTTP client for simulating HTTP requests.
# ---------------------------------------------------------------------------
class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise httpx.HTTPStatusError("Error", request=None, response=self)

class DummyHttpxClient:
    def __init__(self):
        self.calls = []  # record (url, params) for each call

    def get(self, url, params=None):
        self.calls.append((url, params))
        # Simulate different responses based on URL patterns:
        if "Sag(" in url:
            # Simulate a single resource lookup.
            return DummyResponse({"id": 123, "name": "Test Resource"})
        elif "$select" in url:
            # Simulate a general query.
            return DummyResponse({"value": [{"id": 1}, {"id": 2}]})
        elif "gt" in url:
            # Simulate get_latest_updated_ids_since query.
            return DummyResponse({"value": [1, 2, 3]})
        elif "desc" in url:
            # Simulate get_n_latest_updated_ids query.
            return DummyResponse({"value": [4, 5, 6]})
        else:
            return DummyResponse({"value": []})

# ---------------------------------------------------------------------------
# Pytest fixtures to provide a dummy client and a SagQueryClient instance.
# ---------------------------------------------------------------------------
@pytest.fixture
def dummy_client():
    return DummyHttpxClient()

@pytest.fixture
def sag_query_client(dummy_client):
    # Construct a SagQueryClient with a known base_url and the dummy client.
    return SagQueryClient(base_url="https://oda.ft.dk/api", client=dummy_client)

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def test_resource_url(sag_query_client):
    """
    Test that the resource URL is built correctly.
    """
    expected_url = "https://oda.ft.dk/api/Sag"
    assert sag_query_client._resource_url == expected_url

def test_get_single_resource(sag_query_client):
    """
    Test that get() with an id parameter constructs the proper URL
    and returns the simulated single resource.
    """
    result = sag_query_client.get(id="123")
    assert result == {"id": 123, "name": "Test Resource"}

def test_get_query(sag_query_client, dummy_client):
    """
    Test that get() without an id uses the builder's build() method to construct
    the URL. Here, we override builder.build() to return a known URL.
    """
    # Override the builder's build() method to return a test URL.
    sag_query_client.builder.build = lambda: "https://oda.ft.dk/api/Sag?$select=id"
    result = sag_query_client.get()
    # Expect the dummy client to simulate a query response.
    assert result == {"value": [{"id": 1}, {"id": 2}]}
    # Check that the dummy client recorded a call with the expected URL.
    last_call = dummy_client.calls[-1]
    assert last_call[0] == "https://oda.ft.dk/api/Sag?$select=id"

def test_get_latest_updated_ids_since(sag_query_client, dummy_client):
    """
    Test that get_latest_updated_ids_since() builds the expected URL using
    the opdateringsdato mixin functionality and returns the simulated IDs.
    """
    test_timestamp = datetime(2020, 1, 1)
    # Override the builder method to control the URL.
    sag_query_client.builder.build_latest_updated_ids_since_query_url = (
        lambda ts: f"https://oda.ft.dk/api/Sag?$filter=opdateringsdato gt {ts.isoformat()}"
    )
    result = sag_query_client.get_latest_updated_ids_since(test_timestamp)
    assert result == [1, 2, 3]
    # Verify that the dummy client recorded the expected URL.
    last_call = dummy_client.calls[-1]
    expected_url = f"https://oda.ft.dk/api/Sag?$filter=opdateringsdato gt {test_timestamp.isoformat()}"
    assert last_call[0] == expected_url

def test_get_n_latest_updated_ids(sag_query_client, dummy_client):
    """
    Test that get_n_latest_updated_ids() builds the expected URL using
    the opdateringsdato mixin functionality and returns the simulated IDs.
    """
    # Override the builder method to control the URL.
    sag_query_client.builder.build_n_latest_updated_ids_query_url = (
        lambda n: f"https://oda.ft.dk/api/Sag?$orderby=opdateringsdato desc&$top={n}"
    )
    result = sag_query_client.get_n_latest_updated_ids(5)
    assert result == [4, 5, 6]
    # Verify that the dummy client recorded the expected URL.
    last_call = dummy_client.calls[-1]
    expected_url = "https://oda.ft.dk/api/Sag?$orderby=opdateringsdato desc&$top=5"
    assert last_call[0] == expected_url
