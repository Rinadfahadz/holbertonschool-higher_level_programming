#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test a max integer function
    """

    def test_max_integer(self):
        """
        Test the max integer in a list of integers, 
        covering various positions, types, and edge cases.
        """
        # Edge Cases
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([99]), 99) # Single element integer
        self.assertEqual(max_integer([7.7]), 7.7) # Single element float
        self.assertEqual(max_integer([0, 0, 0]), 0) # List of only zeros

        # Basic Positive/Negative/Float Tests
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-4, -3, -2, -1, 0]), 0)
        self.assertEqual(max_integer([-90, -120, -150, -180]), -90)
        self.assertEqual(max_integer([1.0, 1.5, 1.6, 3.7, 2.3]), 3.7)

        # Max in Different Positions (New additions)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)      # Max at the beginning
        self.assertEqual(max_integer([1, 5, 2, 4, 3]), 5)      # Max in the middle
        self.assertEqual(max_integer([10, 5, 10, 2]), 10)      # Duplicate maximum value


    def test_wrong_types(self):
        """
        Test the max integer with wrong parameters types
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Monty", 89, 34, -9.7, "Python"])
        
        # Test list containing different incompatible types (New addition)
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 3])
