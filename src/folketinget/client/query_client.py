from abc import ABC, abstractmethod
import datetime
from typing import Any, List, Protocol
import httpx

from .querybuilder import BaseQueryBuilder, SagQueryBuilder

class QueryClientProtocol(Protocol):
    def get(self, **kwargs: Any) -> Any:
        ...

class BaseQueryClient(ABC):
    def __init__(self, base_url: str, client: httpx.Client = None):
        self.base_url = base_url  # e.g., "https://oda.ft.dk/api"
        self.client = client or httpx.Client()
        self.builder: BaseQueryBuilder = self._create_builder()
    
    @abstractmethod
    def _create_builder(self) -> BaseQueryBuilder:
        """Instantiate and return a query builder for this resource."""
        pass

    @property
    @abstractmethod
    def _resource_endpoint(self) -> str:
        """
        Return the endpoint name for this resource (e.g., "Sag").
        Used to build the resource URL.
        """
        pass
    
    @property
    def _resource_url(self) -> str:
        return f"{self.base_url}/{self._resource_endpoint}"
    
    def get(self, **kwargs: Any) -> Any:
        resource_id = kwargs.pop("id", None)
        if resource_id is not None:
            url = f"{self._resource_url}({resource_id})"
            response = self.client.get(url, params=kwargs)
        else:
            url = self.builder.build()
            response = self.client.get(url, params=kwargs)
        response.raise_for_status()
        return response.json()

class SagQueryClient(BaseQueryClient, QueryClientProtocol):
    @property
    def _resource_endpoint(self) -> str:
        return "Sag"
    
    def _create_builder(self) -> BaseQueryBuilder:
        return SagQueryBuilder(base_url=self.base_url)
    
    def get_latest_updated_ids_since(self, timestamp: datetime.datetime) -> List[int]:
        url = self.builder.build_latest_updated_ids_since_query_url(timestamp)
        data = self.client.get(url).json()
        return data["value"]
        
    def get_n_latest_updated_ids(self, n: int) -> List[int]:
        url = self.builder.build_n_latest_updated_ids_query_url(n)
        data = self.client.get(url).json()
        return data["value"]