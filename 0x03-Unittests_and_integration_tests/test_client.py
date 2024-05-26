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
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """
        This  method tests  GithubOrgClient.org
        and returns correct output
        """
        test_client = GithubOrgClient(org_name)
        response = test_client.org()
        self.assertEqual(response, {"payload": True})
        expected = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(expected)

    @path('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        This tests GithubOrgClients._public_repos_url
        """
        payload = {"repos_url": "https://api.github.com/orgs/octocat/repos"}
        mock_org.return_value = payload
        test_client = GithubOrgClient("octocat")
        self.assertEqual(
            test_client._public_repos_url,
            payload["repos_url"])
