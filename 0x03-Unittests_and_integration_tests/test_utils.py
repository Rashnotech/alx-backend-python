#!/usr/bin/env python3
"""a module that handle unittesting of access map"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    A class that test inherit unittest
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, sequence, expected):
        """test access"""
        self.assertEqual(access_nested_map(nested_map, sequence), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, sequence, expected):
        """test map exception"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, sequence)


class TestGetJson(unittest.TestCase):
    """
    A class that test get json function using unittest.mock patch
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Tests whether get_json correctly processes the response
        from the patch.
        """
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload
        mock_response.status_code = 200
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)





if __name__ == '__main__':
    unittest.main()
