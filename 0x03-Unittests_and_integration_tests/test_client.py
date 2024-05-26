#!/usr/bin/env python3
"""
This module contains
unittests for the
GithubOrgClient
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class, tests
    GithubOrgClient class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """
        This tests  GithubOrgClient.org
        """
        test_client = GithubOrgClient(org_name)
        response = test_client.org()
        self.assertEqual(response, {"payload": True})
        expected = f"https://api.github.com/orgs/{arg_name}"
        mock_get.assert_called_once_with(expected)
