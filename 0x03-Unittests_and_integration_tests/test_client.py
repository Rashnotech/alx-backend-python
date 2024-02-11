#!/usr/bin/env python3
"""a module that parameterize and patch as decorators"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_org, mock_get_json):
        """
        Test public repos method
        """
        mocked_payload = [
                {'name': 'repo1', 'license': {'key': 'MIT'}},
                {'name': 'repo2', 'license': {'key': 'Apache'}}
                ]
        url = 'https://api.github.com/orgs/abc/repos'
        mock_org.return_value = url
        mock_get_json.return_value = mocked_payload

        client = GithubOrgClient('abc')
        result = client.public_repos()
        expected = ['repo1', 'repo2']
        self.assertEqual(result, expected)
        mock_org.assert_called_once()
        mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, mock_license, mock_key, expected):
        """
        Test for has license
        """
        client = GithubOrgClient('abc')
        result = client.has_license(mock_license, mock_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
        }
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    A class that handle integration testing
    """

    @classmethod
    def setUpClass(cls):
        """setup"""
        payload = {
                'https://api.github.com/orgs/google': cls.org_payload,
                'https://api.github.com/orgs/google/repos': cls.repos_payload
                }

        def get_payload(url):
            if url in payload:
                return Mock(**{'json.return_value': payload[url]})
            return HTTPError

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear Down"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """An integration test"""
        org_client = GithubOrgClient('google')
        result = org_client.public_repos()

        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        # Create an instance of GithubOrgClient
        org_client = GithubOrgClient('google')
        result = org_client.public_repos(license='apache-2.0')

        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
