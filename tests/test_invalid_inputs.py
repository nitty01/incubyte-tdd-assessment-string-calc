"""
Test cases for invalid input handling.
These tests cover various invalid input scenarios.
"""
import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'string_calculator'))

from string_calculator import StringCalculator


class TestInvalidInputs(unittest.TestCase):
    """Test cases for invalid input handling."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_non_numeric_string(self):
        """Test that non-numeric strings are handled appropriately."""
        # This test might need to be adjusted based on implementation
        # For now, we'll expect it to handle gracefully
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("abc,def")
    
    def test_mixed_numeric_and_non_numeric(self):
        """Test that mixed numeric and non-numeric strings are handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("1,abc,3")
    
    def test_invalid_custom_delimiter_format(self):
        """Test that invalid custom delimiter format is handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("//\n1,2,3")
    
    def test_missing_newline_after_custom_delimiter(self):
        """Test that missing newline after custom delimiter is handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("//;1;2;3")
    
    def test_empty_custom_delimiter(self):
        """Test that empty custom delimiter is handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("//\n1,2,3")
    
    def test_custom_delimiter_without_numbers(self):
        """Test that custom delimiter without numbers is handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("//;\n")
    
    def test_only_delimiters_no_numbers(self):
        """Test that string with only delimiters and no numbers returns 0."""
        result = self.calculator.add(",,,")
        self.assertEqual(result, 0)
    
    def test_only_newlines_no_numbers(self):
        """Test that string with only newlines and no numbers returns 0."""
        result = self.calculator.add("\n\n\n")
        self.assertEqual(result, 0)
    
    def test_mixed_delimiters_no_numbers(self):
        """Test that string with mixed delimiters and no numbers returns 0."""
        result = self.calculator.add(",\n,\t,")
        self.assertEqual(result, 0)
    
    def test_unicode_characters(self):
        """Test that unicode characters are handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("1,α,3")
    
    def test_very_long_delimiter(self):
        """Test that very long delimiters are handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("//verylongdelimiter\n1verylongdelimiter2")
    
    def test_delimiter_with_spaces(self):
        """Test that delimiters with spaces are handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("// \n1 2 3")
    
    def test_multiple_custom_delimiters(self):
        """Test that multiple custom delimiters are handled appropriately."""
        with self.assertRaises((ValueError, TypeError)):
            self.calculator.add("//;|//*\n1;2*3")


if __name__ == '__main__':
    unittest.main()
