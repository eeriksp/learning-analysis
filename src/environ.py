import os
from types import SimpleNamespace as Object
from urllib.parse import parse_qsl


def get_params(**kwargs: str) -> Object:
    """
    Return a dictionary with the params given as `**kwargs`
    and overriding them with URL query params if running in Voila.

    Unfortunately there is no way to access the URL query params
    in a notebook running in JupyterHub or elsewhere except in Voila.
    """
    params: dict[str, str] = kwargs
    for key, value in parse_qsl(os.environ.get("QUERY_STRING", "")):  # set when running in Voila):
        params[key] = value
    return Object(**params)


def is_voila() -> bool:
    return os.environ.get("QUERY_STRING") is not None
