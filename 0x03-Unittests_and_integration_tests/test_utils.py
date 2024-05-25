#!/usr/bin/env python3
"""
This module contains
unittests
"""
import unittest
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        This Test raises
        the right exception
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class, tests
    get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        This test is a unnitest for get_json
        """
        mock_get.return_value.json.return_value = test_payload

        response = utils.get_json(test_url)
        self.assertEqual(response, test_payload)
        mock_get.assert_called_once_with(test_url)
