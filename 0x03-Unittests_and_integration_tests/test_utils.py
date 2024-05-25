#!/usr/bin/env python3
"""
This module contains
unittests
"""
import unittest
from parameterized import parameterized
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

    @parameterized.expands([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_acces_nested_map_exception(self, nested_map, path):
        """
        This Test raises
        the right exception
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)
