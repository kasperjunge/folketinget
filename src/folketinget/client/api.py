import httpx
from .query_client import SagQueryClient

class Folketinget:
    """Client for the Folketinget API."""
    
    def __init__(self, base_url: str = "https://oda.ft.dk/api", client: httpx.Client = None):
        self.base_url = base_url
        self.client = client or httpx.Client()
        self.sag = SagQueryClient(base_url=self.base_url, client=self.client)
