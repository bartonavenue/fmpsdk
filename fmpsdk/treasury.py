import typing

from .url_methods import __return_json_v4


def treasury(apikey: str,
    from_date: str,
    to_date: str
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /treasury/ API

    All Real-time Treasury Prices.

    :param apikey: Your API key.
    :param from_date: from date.
    :param to_date: to date.
    :return: A list of dictionaries.
    """
    path = f"treasury"
    query_vars = {"apikey": apikey, "from": from_date, "to": to_date}
    return __return_json_v4(path=path, query_vars=query_vars)
