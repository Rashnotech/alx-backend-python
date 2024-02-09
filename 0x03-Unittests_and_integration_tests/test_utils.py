#!/usr/bin/env python3
"""a module that handle unittesting of access map"""
import unittest
from utils import access_nested_map
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
