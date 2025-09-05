"""
Test cases for custom delimiter functionality.
These tests cover handling custom delimiters specified in the input string.
"""
import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'string_calculator'))

from string_calculator import StringCalculator


class TestCustomDelimiters(unittest.TestCase):
    """Test cases for custom delimiter functionality."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_semicolon_delimiter(self):
        """Test that semicolon can be used as a custom delimiter."""
        result = self.calculator.add("//;\n1;2")
        self.assertEqual(result, 3)
    
    def test_pipe_delimiter(self):
        """Test that pipe can be used as a custom delimiter."""
        result = self.calculator.add("//|\n1|2|3")
        self.assertEqual(result, 6)
    
    def test_asterisk_delimiter(self):
        """Test that asterisk can be used as a custom delimiter."""
        result = self.calculator.add("//*\n1*2*3*4")
        self.assertEqual(result, 10)
    
    def test_hash_delimiter(self):
        """Test that hash can be used as a custom delimiter."""
        result = self.calculator.add("//#\n5#10#15")
        self.assertEqual(result, 30)
    
    def test_dollar_delimiter(self):
        """Test that dollar sign can be used as a custom delimiter."""
        result = self.calculator.add("//$\n100$200")
        self.assertEqual(result, 300)
    
    def test_custom_delimiter_with_single_number(self):
        """Test custom delimiter with a single number."""
        result = self.calculator.add("//;\n5")
        self.assertEqual(result, 5)
    
    def test_custom_delimiter_with_zero(self):
        """Test custom delimiter with zero."""
        result = self.calculator.add("//;\n0")
        self.assertEqual(result, 0)
    
    def test_custom_delimiter_with_large_numbers(self):
        """Test custom delimiter with large numbers."""
        result = self.calculator.add("//;\n1000;2000;3000")
        self.assertEqual(result, 6000)
    
    def test_custom_delimiter_with_mixed_case(self):
        """Test custom delimiter with mixed case letters."""
        result = self.calculator.add("//X\n1X2X3")
        self.assertEqual(result, 6)
    
    def test_custom_delimiter_with_special_characters(self):
        """Test custom delimiter with special characters."""
        result = self.calculator.add("//@\n1@2@3")
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
