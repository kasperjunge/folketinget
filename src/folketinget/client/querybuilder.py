from typing import Optional, List, Literal, Generic
from abc import ABC, abstractmethod
from datetime import datetime
from .protocols import FIELD, ODataQueryable
from .fields import SagBaseFields

ModelType = Literal[
    "Aktstykke",
    "Almdel",
    "Debat",
    "Emneord",
    "Emneordstype",
    "EUsag",
    "Forslag",
    "Sag",
    "Sagskategori",
    "Sagsstatus",
    "Sagstype",
    "Sambehandlinger",
]


class DuplicateExpressionNotAllowed(ValueError):

    def __init__(self, expression_name: str):
        super().__init__(
            f"{expression_name.title()} can only be used ones in query expression."
        )


class BaseQueryBuilder(ABC, Generic[FIELD], ODataQueryable[FIELD]):
    def __init__(
        self,
        base_url: str = "https://oda.ft.dk/api",
    ):
        self._base_url = base_url + "/" + self._model_type
        self._expand: List[str] = []
        self._filter: Optional[str] = None
        self._orderby: List[str] = []
        self._skip: Optional[int] = None
        self._top: Optional[int] = None
        self._select: List[str] = []

    @property
    @abstractmethod
    def _model_type(cls) -> ModelType:
        pass

    def expand(self, *fields: FIELD) -> "BaseQueryBuilder":
        """
        Adds fields to the list of $expand parameters.
        """
        if self._expand:
            raise DuplicateExpressionNotAllowed("Expand")
        self._expand.extend(fields)
        return self

    def filter(self, criteria: str) -> "BaseQueryBuilder":
        """
        Sets the $filter parameter.
        """
        if self._filter:
            raise DuplicateExpressionNotAllowed("Filter")
        self._filter = criteria
        return self

    def orderby(self, *fields: FIELD) -> "BaseQueryBuilder":
        """
        Adds fields to the list of $orderby parameters.
        """
        if self._orderby:
            raise DuplicateExpressionNotAllowed("OrderBy")
        self._orderby.extend(fields)
        return self

    def skip(self, count: int) -> "BaseQueryBuilder":
        """
        Sets the $skip parameter.
        """
        if self._skip:
            raise DuplicateExpressionNotAllowed("Skip")
        self._skip = count
        return self

    def top(self, count: int) -> "BaseQueryBuilder":
        """
        Sets the $top parameter.
        """
        if self._top:
            raise DuplicateExpressionNotAllowed("Top")
        self._top = count
        return self

    def select(self, *fields: FIELD) -> "BaseQueryBuilder":
        """
        Adds fields to the list of $select parameters.
        """
        if self._select:
            raise DuplicateExpressionNotAllowed("Select")
        self._select.extend(fields)
        return self

    def build(self) -> str:
        """
        Builds the final query URL with the specified parameters.
        """
        query_parts = []

        if self._expand:
            query_parts.append(f"$expand={','.join(self._expand)}")

        if self._filter:
            query_parts.append(f"$filter={self._filter}")

        if self._orderby:
            query_parts.append(f"$orderby={','.join(self._orderby)}")

        if self._skip is not None:
            query_parts.append(f"$skip={self._skip}")

        if self._top is not None:
            query_parts.append(f"$top={self._top}")

        if self._select:
            query_parts.append(f"$select={','.join(self._select)}")

        if not query_parts:
            return self._base_url

        query_string = "&".join(query_parts)

        return f"{self._base_url}?{query_string}"

class OpdateringsdatoQueryBuilderMixin:
    @property
    def opdateringsdato_column(self) -> str:
        return "opdateringsdato"
    
    def build_latest_updated_ids_since_query_url(self, timestamp: datetime) -> str:
        self.filter(f"{self.opdateringsdato_column} gt datetime'{timestamp.isoformat()}'")
        return self.build()
    
    def build_n_latest_updated_ids_query_url(self, n: int) -> str:
        self.orderby(f"{self.opdateringsdato_column} desc").top(n)
        return self.build()

class SagQueryBuilder(BaseQueryBuilder[SagBaseFields], OpdateringsdatoQueryBuilderMixin):
    _model_type = "Sag"

