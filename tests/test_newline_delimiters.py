"""
Test cases for newline delimiter functionality.
These tests cover handling newlines as delimiters between numbers.
"""
import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'string_calculator'))

from string_calculator import StringCalculator


class TestNewlineDelimiters(unittest.TestCase):
    """Test cases for newline delimiter functionality."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_newline_as_delimiter(self):
        """Test that newlines can be used as delimiters."""
        result = self.calculator.add("1\n2")
        self.assertEqual(result, 3)
    
    def test_mixed_comma_and_newline_delimiters(self):
        """Test that both commas and newlines can be used as delimiters."""
        result = self.calculator.add("1\n2,3")
        self.assertEqual(result, 6)
    
    def test_multiple_newlines(self):
        """Test that multiple newlines work as delimiters."""
        result = self.calculator.add("1\n2\n3\n4")
        self.assertEqual(result, 10)
    
    def test_newline_at_beginning(self):
        """Test that newline at the beginning is handled correctly."""
        result = self.calculator.add("\n1,2")
        self.assertEqual(result, 3)
    
    def test_newline_at_end(self):
        """Test that newline at the end is handled correctly."""
        result = self.calculator.add("1,2\n")
        self.assertEqual(result, 3)
    
    def test_consecutive_newlines(self):
        """Test that consecutive newlines are handled correctly."""
        result = self.calculator.add("1\n\n2")
        self.assertEqual(result, 3)
    
    def test_only_newlines(self):
        """Test that string with only newlines returns 0."""
        result = self.calculator.add("\n\n")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
