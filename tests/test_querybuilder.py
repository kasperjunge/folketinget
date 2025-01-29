from folketinget import Sag


def test_sag_orderby_skip_select():

    sag = Sag()
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
