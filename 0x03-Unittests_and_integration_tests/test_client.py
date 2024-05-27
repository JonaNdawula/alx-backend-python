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

    @patch('client.get_json',
           return_value=[{"name": "repo1"}, {"name": "repo2"}])
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_reposs(self, mock_public_repos_url, mock_get_json):
        """
        This tests GithubOrgClient.public_repos
        """
        mock_public_repos_url.return_value =
        "https://api.github.com/orgs/octocat/repos"
        test_client = GithubOrgClient("octocat")
        self.assertEqual(test_client.public_repos(), ["repo1", "repo2"])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()
