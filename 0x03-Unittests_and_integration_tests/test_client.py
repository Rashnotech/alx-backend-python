#!/usr/bin/env python3
"""a module that parameterize and patch as decorators"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    A class that test github client
    """

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc')
        ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_url, mock_get_json):
        """
        Test that GithubOrgClient returns the correct value and url
        """
        mock_response = {"key": "value"}
        mock_get_json.return_value = mock_response
        client = GithubOrgClient(org_name)

        # Assertions
        self.assertEqual(client.org, mock_response)
        mock_get_json.assert_called_once_with(expected_url)

    
    @patch('client.get_json')
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org, mock_get_json):
        """Test public repos url method"""
        mocked_payload = {'repos_url': 'https://github.com/orgs/abc/repos'}
        mock_org.return_value = mocked_payload

        # Create an instance of the client
        client = GithubOrgClient('abc')

        # Call the method under test
        actual_url = client._public_repos_url

        # Assertion
        self.assertEqual(actual_url, mocked_payload['repos_url'])

    
    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_org, mock_get_json):
        """
        Test public repos method
        """
        mocked_payload = [
                {'name': 'repo1', 'license': {'key': 'MIT'}},
                {'name': 'repo2', 'license': {'key': 'Apache'}}
                ]
        mock_org.return_value = 'https://api.github.com/orgs/abc/repos'
        mock_get_json.return_value = mocked_payload

        client = GithubOrgClient('abc')
        result = client.public_repos()

        expected = ['repo1', 'repo2']
        self.assertEqual(result, expected)
        mock_org.assert_called_once()
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/abc/repos')


if __name__ == '__main__':
    unittest.main()
