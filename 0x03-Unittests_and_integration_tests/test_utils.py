#!/usr/bin/env python3
"""a module that handle unittesting of access map"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """
    A class that test memoization
    """
    def test_memoize(self):
        """
        Test if a method is call one and property is call twice
        """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            # Calling a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Asserting that a_method is only called once
            mock_a_method.assert_called_once()

            # Asserting the correct result is returned
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
