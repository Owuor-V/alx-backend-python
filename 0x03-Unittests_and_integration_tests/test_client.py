#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, payload, mock_get_json):
        """Test GithubOrgClient.org returns expected result"""
        mock_get_json.return_value = payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url returns expected result"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": "http://mocked_url"}
            client = GithubOrgClient("dummy")
            self.assertEqual(client._public_repos_url, "http://mocked_url")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns expected list of repos"""
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = mock_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = "http://mocked_url"

            client = GithubOrgClient("dummy")
            result = client.public_repos()

            # Verify repos list matches expected repo names
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Verify mocks called once
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("http://mocked_url")
