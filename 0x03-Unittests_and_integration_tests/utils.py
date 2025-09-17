#!/usr/bin/env python3

import requests
from typing import Mapping, Any, Sequence


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> dict:
    response = requests.get(url)
    return response.json()
