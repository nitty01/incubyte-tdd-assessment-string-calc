"""
Test cases for edge cases and boundary conditions.
These tests cover various edge cases that might occur in real usage.
"""
import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'string_calculator'))

from string_calculator import StringCalculator


class TestEdgeCases(unittest.TestCase):
    """Test cases for edge cases and boundary conditions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_whitespace_around_numbers(self):
        """Test that whitespace around numbers is handled correctly."""
        result = self.calculator.add(" 1 , 2 , 3 ")
        self.assertEqual(result, 6)
    
    def test_tabs_as_delimiters(self):
        """Test that tabs can be used as delimiters."""
        result = self.calculator.add("1\t2\t3")
        self.assertEqual(result, 6)
    
    def test_mixed_whitespace_delimiters(self):
        """Test that mixed whitespace characters work as delimiters."""
        result = self.calculator.add("1 \t\n 2 \t\n 3")
        self.assertEqual(result, 6)
    
    def test_very_large_numbers(self):
        """Test that very large numbers are handled correctly."""
        result = self.calculator.add("999999,1000000")
        self.assertEqual(result, 1999999)
    
    def test_decimal_numbers(self):
        """Test that decimal numbers are handled correctly."""
        result = self.calculator.add("1.5,2.5")
        self.assertEqual(result, 4)
    
    def test_very_long_string(self):
        """Test that very long strings with many numbers work correctly."""
        numbers = ",".join([str(i) for i in range(1, 101)])  # 1 to 100
        result = self.calculator.add(numbers)
        self.assertEqual(result, 5050)  # Sum of 1 to 100
    
    def test_single_character_delimiter(self):
        """Test that single character delimiters work correctly."""
        result = self.calculator.add("//a\n1a2a3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_special_regex_characters(self):
        """Test that delimiters with special regex characters work correctly."""
        result = self.calculator.add("//.\n1.2.3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_plus_sign(self):
        """Test that delimiters with plus sign work correctly."""
        result = self.calculator.add("//+\n1+2+3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_question_mark(self):
        """Test that delimiters with question mark work correctly."""
        result = self.calculator.add("//?\n1?2?3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_parentheses(self):
        """Test that delimiters with parentheses work correctly."""
        result = self.calculator.add("//()\n1()2()3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_square_brackets(self):
        """Test that delimiters with square brackets work correctly."""
        result = self.calculator.add("//[]\n1[]2[]3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_curly_braces(self):
        """Test that delimiters with curly braces work correctly."""
        result = self.calculator.add("//{}\n1{}2{}3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_backslash(self):
        """Test that delimiters with backslash work correctly."""
        result = self.calculator.add("//\\\n1\\2\\3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_caret(self):
        """Test that delimiters with caret work correctly."""
        result = self.calculator.add("//^\n1^2^3")
        self.assertEqual(result, 6)
    
    def test_delimiter_with_dollar_sign(self):
        """Test that delimiters with dollar sign work correctly."""
        result = self.calculator.add("//$\n1$2$3")
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
