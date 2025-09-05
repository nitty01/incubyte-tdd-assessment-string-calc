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
            ValueError: If negative numbers are found or invalid format
        """
        if not numbers or not numbers.strip():
            return 0
        
        # Extract custom delimiters and numbers
        delimiters, numbers_part = self._extract_custom_delimiters(numbers)
        
        # Validate input format (no trailing delimiters)
        self._validate_input_format(numbers_part, delimiters)
        
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
            numbers: Input string that may contain custom delimiter specification
            
        Returns:
            Tuple of (delimiters_list, numbers_string)
        """
        # Default delimiters
        delimiters = [',', '\n']
        
        # Check if custom delimiters are specified
        if numbers.startswith('//'):
            # Find the end of delimiter specification
            newline_pos = numbers.find('\n')
            if newline_pos == -1:
                raise ValueError("Invalid custom delimiter format")
            
            # Extract delimiter specification
            delimiter_spec = numbers[2:newline_pos]
            numbers_part = numbers[newline_pos + 1:]
            
            # Parse custom delimiters
            custom_delimiters = self._parse_custom_delimiters(delimiter_spec)
            delimiters = custom_delimiters
        else:
            numbers_part = numbers
        
        return delimiters, numbers_part
    
    def _parse_custom_delimiters(self, delimiter_spec: str) -> List[str]:
        """
        Parse custom delimiter specification.
        
        Args:
            delimiter_spec: String containing delimiter specification
            
        Returns:
            List of delimiter strings
        """
        delimiters = []
        
        # Handle multiple delimiters in brackets [delim1][delim2]
        pattern = r'\[([^\]]+)\]'
        matches = re.findall(pattern, delimiter_spec)
        
        if matches:
            # Multiple delimiters specified
            delimiters.extend(matches)
        else:
            # Single delimiter specified
            delimiters.append(delimiter_spec)
        
        return delimiters
    
    def _validate_input_format(self, numbers: str, delimiters: List[str]) -> None:
        """
        Validate that the input format is correct (no trailing delimiters).
        
        Args:
            numbers: String containing numbers
            delimiters: List of delimiter strings
            
        Raises:
            ValueError: If input format is invalid
        """
        if not numbers or not numbers.strip():
            return
        
        # Check for trailing delimiters - only validate if there are actual numbers
        # This allows cases like "1,2\n" (newline at end) but catches "1,\n" (comma followed by newline)
        if numbers.strip():
            # Check for specific invalid patterns like "1,\n" (comma followed by newline)
            for delimiter in delimiters:
                if delimiter == ',':
                    # Check for comma followed by newline pattern
                    if re.search(r',\s*\n\s*$', numbers):
                        raise ValueError("Invalid input: trailing delimiter ',' not allowed")
                elif delimiter == '\n':
                    # Allow newline at end, but check for comma before newline
                    if re.search(r',\s*\n\s*$', numbers):
                        raise ValueError("Invalid input: trailing delimiter ',' not allowed")
    
    def _parse_numbers(self, numbers: str, delimiters: List[str]) -> List[int]:
        """
        Parse numbers from string using specified delimiters.
        
        Args:
            numbers: String containing numbers
            delimiters: List of delimiter strings
            
        Returns:
            List of parsed integers
            
        Raises:
            ValueError: If any non-integer numbers are found
        """
        if not numbers or not numbers.strip():
            return []
        
        # Create regex pattern for all delimiters
        # Escape special regex characters in delimiters
        escaped_delimiters = [re.escape(delim) for delim in delimiters]
        pattern = '|'.join(escaped_delimiters)
        
        # Split by delimiters and convert to integers
        number_strings = re.split(pattern, numbers)
        
        # Filter out empty strings and validate each number
        number_list = []
        for num_str in number_strings:
            if num_str.strip():  # Skip empty strings
                stripped_num = num_str.strip()
                
                # Check if the number contains decimal point
                if '.' in stripped_num:
                    raise ValueError(f"Invalid input: decimal numbers not allowed: {stripped_num}")
                
                # Check if the number contains any non-digit characters (except minus sign at start)
                if not re.match(r'^-?\d+$', stripped_num):
                    raise ValueError(f"Invalid input: non-integer number not allowed: {stripped_num}")
                
                try:
                    number_list.append(int(stripped_num))
                except ValueError as e:
                    raise ValueError(f"Invalid input: cannot convert to integer: {stripped_num}")
        
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


if __name__ == '__main__':
    str_calc = StringCalculator()
    print(str_calc.add("1\n2,3,10"))
