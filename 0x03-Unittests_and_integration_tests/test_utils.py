#!/usr/bin/env python3

import unittest
from parameterized import parameterized

def access_nested_map(nested_map, path):
    """Access a nested map with a path of keys"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected) -> None:
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
