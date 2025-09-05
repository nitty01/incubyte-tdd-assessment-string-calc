"""
Comprehensive test runner for String Calculator TDD Kata.
This module provides utilities to run all tests and generate reports.
"""
import unittest
import sys
import os
from io import StringIO


class TestRunner:
    """Test runner for String Calculator tests."""
    
    def __init__(self):
        self.test_suites = [
            'test_basic_calculations',
            'test_newline_delimiters', 
            'test_custom_delimiters',
            'test_negative_numbers',
            'test_edge_cases',
            'test_invalid_inputs'
        ]
    
    def run_all_tests(self, verbosity=2):
        """Run all test suites and return the result."""
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        # Add all test modules
        for test_module in self.test_suites:
            try:
                module = __import__(test_module)
                tests = loader.loadTestsFromModule(module)
                suite.addTests(tests)
            except ImportError as e:
                print(f"Warning: Could not import {test_module}: {e}")
        
        # Run tests
        runner = unittest.TextTestRunner(verbosity=verbosity)
        result = runner.run(suite)
        
        return result
    
    def run_specific_test_suite(self, test_suite_name, verbosity=2):
        """Run a specific test suite."""
        if test_suite_name not in self.test_suites:
            raise ValueError(f"Test suite '{test_suite_name}' not found. Available: {self.test_suites}")
        
        loader = unittest.TestLoader()
        module = __import__(test_suite_name)
        suite = loader.loadTestsFromModule(module)
        
        runner = unittest.TextTestRunner(verbosity=verbosity)
        result = runner.run(suite)
        
        return result
    
    def get_test_summary(self):
        """Get a summary of all available tests."""
        summary = {
            'total_test_suites': len(self.test_suites),
            'test_suites': self.test_suites,
            'test_categories': {
                'Basic Calculations': 'test_basic_calculations',
                'Newline Delimiters': 'test_newline_delimiters',
                'Custom Delimiters': 'test_custom_delimiters', 
                'Negative Numbers': 'test_negative_numbers',
                'Edge Cases': 'test_edge_cases',
                'Invalid Inputs': 'test_invalid_inputs'
            }
        }
        return summary


def main():
    """Main function to run tests."""
    runner = TestRunner()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--summary':
            summary = runner.get_test_summary()
            print("String Calculator TDD Kata - Test Summary")
            print("=" * 50)
            print(f"Total Test Suites: {summary['total_test_suites']}")
            print("\nTest Categories:")
            for category, module in summary['test_categories'].items():
                print(f"  - {category}: {module}")
            return
        
        elif sys.argv[1] == '--suite' and len(sys.argv) > 2:
            suite_name = sys.argv[2]
            print(f"Running test suite: {suite_name}")
            result = runner.run_specific_test_suite(suite_name)
        else:
            print("Usage: python test_runner.py [--summary] [--suite <suite_name>]")
            return
    else:
        print("Running all String Calculator tests...")
        result = runner.run_all_tests()
    
    # Print summary
    if result.wasSuccessful():
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ {len(result.failures)} failures, {len(result.errors)} errors")
        
        if result.failures:
            print("\nFailures:")
            for test, traceback in result.failures:
                print(f"  - {test}: {traceback}")
        
        if result.errors:
            print("\nErrors:")
            for test, traceback in result.errors:
                print(f"  - {test}: {traceback}")


if __name__ == '__main__':
    main()
