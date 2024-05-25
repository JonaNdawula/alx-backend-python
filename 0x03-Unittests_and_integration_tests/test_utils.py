#!/usr/bin/env python3
"""
This module contains
unittets
"""
import unittest
from parametized import parametized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class, tests
    Map functions
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests if method returnscorrect
        output
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
