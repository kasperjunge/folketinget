import pytest
from datetime import datetime
from folketinget.models.sag import Sag
from folketinget.client.querybuilder import SagQueryBuilder, DuplicateExpressionNotAllowed



def test_sag_orderby_skip_select():

    sag = SagQueryBuilder()
    url = (
        sag.orderby("afgørelsesdato", "opdateringsdato")
        .skip(10)
        .select("afgørelse", "id", "titel")
        .build()
    )
    expected_url_string = "https://oda.ft.dk/api/Sag?$orderby=afgørelsesdato,opdateringsdato&$skip=10&$select=afgørelse,id,titel"

    assert (
        url == expected_url_string
    ), f"Expected url string '{expected_url_string}' but got '{url}'."


def test_duplicate_expand_raises_exception():
    builder = SagQueryBuilder(base_url="https://oda.ft.dk/api")
    builder.expand("field1")
    with pytest.raises(DuplicateExpressionNotAllowed) as excinfo:
        builder.expand("field2")
    assert "Expand" in str(excinfo.value)

def test_duplicate_filter_raises_exception():
    builder = SagQueryBuilder(base_url="https://oda.ft.dk/api")
    builder.filter("name eq 'test'")
    with pytest.raises(DuplicateExpressionNotAllowed) as excinfo:
        builder.filter("age gt 20")
    assert "Filter" in str(excinfo.value)

def test_duplicate_skip_raises_exception():
    builder = SagQueryBuilder(base_url="https://oda.ft.dk/api")
    builder.skip(5)
    with pytest.raises(DuplicateExpressionNotAllowed) as excinfo:
        builder.skip(10)
    assert "Skip" in str(excinfo.value)

def test_duplicate_top_raises_exception():
    builder = SagQueryBuilder(base_url="https://oda.ft.dk/api")
    builder.top(10)
    with pytest.raises(DuplicateExpressionNotAllowed) as excinfo:
        builder.top(20)
    assert "Top" in str(excinfo.value)

def test_duplicate_select_raises_exception():
    builder = SagQueryBuilder(base_url="https://oda.ft.dk/api")
    builder.select("field1")
    with pytest.raises(DuplicateExpressionNotAllowed) as excinfo:
        builder.select("field2")
    assert "Select" in str(excinfo.value)

def test_build_latest_updated_ids_query_url_with_select():
    builder = SagQueryBuilder(base_url="https://oda.ft.dk/api")
    # First, include the required opdateringsdato column.
    builder.select("opdateringsdato")
    test_timestamp = datetime(2023, 1, 1, 12, 0, 0)
    url = builder.build_latest_updated_ids_since_query_url(test_timestamp)
    expected_filter = f"$filter=opdateringsdato gt {test_timestamp.isoformat()}"
    assert expected_filter in url
    assert url.startswith("https://oda.ft.dk/api/Sag?")

def test_build_n_latest_updated_ids_query_url_with_select():
    builder = SagQueryBuilder(base_url="https://oda.ft.dk/api")
    builder.select("opdateringsdato")
    n = 5
    url = builder.build_n_latest_updated_ids_query_url(n)
    expected_orderby = "$orderby=opdateringsdato desc"
    expected_top = f"$top={n}"
    assert expected_orderby in url
    assert expected_top in url
    assert url.startswith("https://oda.ft.dk/api/Sag?")