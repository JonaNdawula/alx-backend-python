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
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        This tests GithubOrgClient.public_repos
        """
        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/octocat/repos"
        test_client = GithubOrgClient("octocat")
        self.assertEqual(test_client.public_repos(), ["repo1", "repo2"])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        This method tests GithubOrgClient.has_license
        """
        test_client = GithubOrgClient("octocat")
        self.assertEqual(test_client.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": org_payload,
     "repos_payload": repos_payload,
     "expected_repos": expected_repos,
     "apache2_repos": apache2_repos
     }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    TestIntegrationGithubOrgClient class, tests
    GithubOrg class
    """

    @classmethod
    def setUpClass(cls):
        """
        This method sets up the test class
        """
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()

        def side_effect(url):
            """
            Is a class method returning Mock
            """
            if url.endswith("/orgs/octocat"):
                return Mock(json=lambda: cls.org_payload)
            if url.endswith("/orgs/octocat/repos"):
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: {})

        cls.get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        This method tears down the test class
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        This tests GithubOrgClient.public_repos
        """
        test_client = GithubOrgClient("octocat")
        self.assertEqual(test_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        This tests GithubOrgClient. public_repos
        with license
        """
        test_client = GithubOrgClient("octocat")
        self.assertEqual(
            test_client.public_repos("apache-2.0"),
            self.apache2_repos
        )
