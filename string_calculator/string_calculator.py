import re
from typing import List


class StringCalculator:
    """
    A simple string calculator that performs addition on comma-separated numbers.
    
    This class implements the String Calculator Kata with all 9 requirements:
    1. Basic addition with up to 2 numbers
    2. Arbitrary number of numbers
    3. Newline separators
    4. Custom delimiters
    5. Negative number validation
    6. Numbers > 1000 ignored
    7. Arbitrary length delimiters
    8. Multiple single-length delimiters
    9. Multiple longer-length delimiters
    """
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string input.
        
        Args:
            numbers: A string containing numbers separated by delimiters
            
        Returns:
            The sum of all numbers (ignoring numbers > 1000)
            
        Raises:
            ValueError: If negative numbers are found
        """
        if not numbers or not numbers.strip():
            return 0
        
        # Extract custom delimiters and numbers
        delimiters, numbers_part = self._extract_custom_delimiters(numbers)
        
        # Parse numbers using the delimiters
        number_list = self._parse_numbers(numbers_part, delimiters)
        
        # Validate for negative numbers
        self._validate_negative_numbers(number_list)
        
        # Filter out numbers > 1000 and sum
        filtered_numbers = [num for num in number_list if num <= 1000]
        return sum(filtered_numbers)
    
    def _extract_custom_delimiters(self, numbers: str) -> tuple[List[str], str]:
        """
        Extract custom delimiters from the input string.
        
        Args:
            numbers: Input string that may contain custom delimiters
            
        Returns:
            Tuple of (delimiters_list, numbers_part)
        """
        # Default delimiters
        delimiters = [',', '\n']
        
        # Check if custom delimiters are specified
        if numbers.startswith('//'):
            # Find the end of delimiter specification
            newline_pos = numbers.find('\n')
            if newline_pos == -1:
                # No newline found, treat entire string as numbers
                return delimiters, numbers
            
            delimiter_spec = numbers[2:newline_pos]
            numbers_part = numbers[newline_pos + 1:]
            
            # Parse custom delimiters
            custom_delimiters = self._parse_custom_delimiters(delimiter_spec)
            delimiters.extend(custom_delimiters)
            
            return delimiters, numbers_part
        
        return delimiters, numbers
    
    def _parse_custom_delimiters(self, delimiter_spec: str) -> List[str]:
        """
        Parse custom delimiters from delimiter specification.
        
        Args:
            delimiter_spec: String containing delimiter specifications
            
        Returns:
            List of custom delimiters
        """
        delimiters = []
        
        # Handle multiple delimiters in format [delim1][delim2]...
        pattern = r'\[([^\]]+)\]'
        matches = re.findall(pattern, delimiter_spec)
        
        if matches:
            # Multiple delimiters specified
            delimiters.extend(matches)
        else:
            # Single delimiter specified
            delimiters.append(delimiter_spec)
        
        return delimiters
    
    def _parse_numbers(self, numbers: str, delimiters: List[str]) -> List[int]:
        """
        Parse numbers from string using specified delimiters.
        
        Args:
            numbers: String containing numbers
            delimiters: List of delimiter strings
            
        Returns:
            List of parsed integers
        """
        if not numbers or not numbers.strip():
            return []
        
        # Create regex pattern for all delimiters
        # Escape special regex characters in delimiters
        escaped_delimiters = [re.escape(delim) for delim in delimiters]
        pattern = '|'.join(escaped_delimiters)
        
        # Split by delimiters and convert to integers
        number_strings = re.split(pattern, numbers)
        
        # Filter out empty strings and convert to integers
        number_list = []
        for num_str in number_strings:
            if num_str.strip():  # Skip empty strings
                try:
                    number_list.append(int(num_str.strip()))
                except ValueError:
                    # Skip invalid numbers
                    continue
        
        return number_list
    
    def _validate_negative_numbers(self, numbers: List[int]) -> None:
        """
        Validate that no negative numbers are present.
        
        Args:
            numbers: List of numbers to validate
            
        Raises:
            ValueError: If any negative numbers are found
        """
        negative_numbers = [num for num in numbers if num < 0]
        
        if negative_numbers:
            error_message = f"negative numbers not allowed: {' '.join(map(str, negative_numbers))}"
            raise ValueError(error_message)
