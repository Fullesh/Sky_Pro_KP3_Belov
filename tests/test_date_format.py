from src.date_format import format_date


def test_date_format():
    assert format_date("2018-04-04T17:33:34.701093") == '04.04.2018'
    