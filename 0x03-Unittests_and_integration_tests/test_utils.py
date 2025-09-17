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
        """
        Test that access_nested_map returns the expected result
        for different nested maps and paths.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple) -> None:
        """
        Test that access_nested_map raises a KeyError for missing keys.
        Also validates that the exception message matches the missing key.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


if __name__ == "__main__":
    unittest.main()
