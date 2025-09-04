"""
Test cases for basic string calculator functionality.
These tests cover the fundamental requirements of the String Calculator.
"""
import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'string_calculator'))

from ..string_calculator import StringCalculator


class TestBasicCalculations(unittest.TestCase):
    """Test cases for basic calculation functionality."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0."""
        result = self.calculator.add("")
        self.assertEqual(result, 0)
    
    def test_single_number_returns_itself(self):
        """Test that a single number returns itself."""
        result = self.calculator.add("1")
        self.assertEqual(result, 1)
    
    def test_two_numbers_comma_separated(self):
        """Test that two comma-separated numbers return their sum."""
        result = self.calculator.add("1,5")
        self.assertEqual(result, 6)
    
    def test_multiple_numbers_comma_separated(self):
        """Test that multiple comma-separated numbers return their sum."""
        result = self.calculator.add("1,2,3,4,5")
        self.assertEqual(result, 15)
    
    def test_zero_numbers(self):
        """Test that zero is handled correctly."""
        result = self.calculator.add("0")
        self.assertEqual(result, 0)
    
    def test_large_numbers(self):
        """Test that large numbers are handled correctly."""
        result = self.calculator.add("1000,2000,3000")
        self.assertEqual(result, 6000)


if __name__ == '__main__':
    unittest.main()
