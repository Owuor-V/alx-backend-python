#!/usr/bin/env python3
"""Utility functions for nested maps, HTTP requests, and memoization"""

import requests
from typing import Mapping, Any, Sequence, Dict, Callable


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a nested map with a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Dict:
    """Fetch JSON content from a URL."""
    response = requests.get(url)
    return response.json()


def memoize(method: Callable) -> Callable:
    """Decorator to cache method results (memoization)."""
    attr_name = "_memoize_" + method.__name__

    def memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)
    return memoized
