"""
Test cases for negative number handling.
These tests cover exception handling for negative numbers.
"""
import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'string_calculator'))

from string_calculator import StringCalculator


class TestNegativeNumbers(unittest.TestCase):
    """Test cases for negative number handling."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = StringCalculator()
    
    def test_single_negative_number_throws_exception(self):
        """Test that a single negative number throws an exception."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1")
        
        self.assertIn("negative numbers not allowed", str(context.exception))
        self.assertIn("-1", str(context.exception))
    
    def test_multiple_negative_numbers_throws_exception(self):
        """Test that multiple negative numbers throw an exception with all negatives listed."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3,-4")
        
        exception_message = str(context.exception)
        self.assertIn("negative numbers not allowed", exception_message)
        self.assertIn("-2", exception_message)
        self.assertIn("-4", exception_message)
    
    def test_all_negative_numbers_throws_exception(self):
        """Test that all negative numbers throw an exception."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1,-2,-3")
        
        exception_message = str(context.exception)
        self.assertIn("negative numbers not allowed", exception_message)
        self.assertIn("-1", exception_message)
        self.assertIn("-2", exception_message)
        self.assertIn("-3", exception_message)
    
    def test_negative_number_with_custom_delimiter(self):
        """Test that negative numbers with custom delimiter throw an exception."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("//;\n1;-2;3")
        
        exception_message = str(context.exception)
        self.assertIn("negative numbers not allowed", exception_message)
        self.assertIn("-2", exception_message)
    
    def test_negative_number_with_newlines(self):
        """Test that negative numbers with newlines throw an exception."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1\n-2\n3")
        
        exception_message = str(context.exception)
        self.assertIn("negative numbers not allowed", exception_message)
        self.assertIn("-2", exception_message)
    
    def test_multiple_negative_numbers_with_mixed_delimiters(self):
        """Test that multiple negative numbers with mixed delimiters throw an exception."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("//;\n1;-2\n3;-4")
        
        exception_message = str(context.exception)
        self.assertIn("negative numbers not allowed", exception_message)
        self.assertIn("-2", exception_message)
        self.assertIn("-4", exception_message)
    
    def test_zero_and_negative_numbers(self):
        """Test that zero and negative numbers are handled correctly."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("0,-1,2")
        
        exception_message = str(context.exception)
        self.assertIn("negative numbers not allowed", exception_message)
        self.assertIn("-1", exception_message)
    
    def test_large_negative_numbers(self):
        """Test that large negative numbers throw an exception."""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1000,-2000")
        
        exception_message = str(context.exception)
        self.assertIn("negative numbers not allowed", exception_message)
        self.assertIn("-1000", exception_message)
        self.assertIn("-2000", exception_message)


if __name__ == '__main__':
    unittest.main()
