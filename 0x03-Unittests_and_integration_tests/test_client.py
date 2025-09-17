#!/usr/bin/env python3
"""Unittests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):

        # Test that GithubOrgClient.org returns the expected value.


        test_payload = {"payload": True}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):

        test_payload = {"repos_url": "https://api.github.com/orgs/test/repos"}
        with patch.object(GithubOrgClient, "org", new_callable=property) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("test")
            result = client._public_repos_url
            self.assertEqual(result, test_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
