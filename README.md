# String Calculator TDD Kata

A complete implementation of the String Calculator Kata with a modern web UI for testing.

## Features

This implementation covers all 9 requirements of the String Calculator Kata:

1. **Basic addition** - Handle up to 2 numbers separated by commas
2. **Arbitrary numbers** - Handle unknown amount of numbers
3. **Newline separators** - Support newlines as delimiters
4. **Custom delimiters** - Support custom delimiters with `//delimiter\n` format
5. **Negative validation** - Throw exception for negative numbers
6. **Large number filtering** - Ignore numbers > 1000
7. **Arbitrary length delimiters** - Support delimiters of any length with `[delimiter]` format
8. **Multiple delimiters** - Support multiple single-length delimiters
9. **Multiple longer delimiters** - Support multiple delimiters of any length

## Quick Start

### Option 1: Using the run script (Recommended)

```bash
./run.sh
```

This script will:
- Check Python 3 installation
- Create a virtual environment
- Install dependencies
- Run tests (optional)
- Start the web UI

### Option 2: Manual setup

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests:**
   ```bash
   python3 tests/test_runner.py
   ```

4. **Start web UI:**
   ```bash
   cd ui
   python3 app.py
   ```

5. **Open browser:**
   Navigate to `http://localhost:5000`

## Usage Examples

### Basic Usage
- Empty string: `""` → `0`
- Single number: `"1"` → `1`
- Two numbers: `"1,2"` → `3`
- Multiple numbers: `"1,2,3,4,5"` → `15`

### Newline Separators
- Mixed delimiters: `"1\n2,3"` → `6`

### Custom Delimiters
- Semicolon: `"//;\n1;2;3"` → `6`
- Multiple delimiters: `"//[*][%]\n1*2%3"` → `6`
- Arbitrary length: `"//[***]\n1***2***3"` → `6`

### Large Numbers
- Filtering: `"1001,2,3000"` → `2` (ignores numbers > 1000)

### Error Handling
- Negative numbers: `"1,-2,3"` → `ValueError: negative numbers not allowed: -2`

## Project Structure

```
incubyte-tdd-assessment-string-calc/
├── string_calculator/
│   └── string_calculator.py      # Main implementation
├── tests/
│   ├── test_runner.py            # Test runner
│   ├── test_basic_calculations.py
│   ├── test_negative_numbers.py
│   ├── test_custom_delimiters.py
│   ├── test_newline_delimiters.py
│   ├── test_edge_cases.py
│   └── test_invalid_inputs.py
├── ui/
│   ├── app.py                    # Flask web application
│   └── templates/
│       └── index.html           # Web UI template
├── run.sh                       # Setup and run script
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Web UI Features

The web interface provides:
- **Interactive calculator** - Enter numbers and see results instantly
- **Example calculations** - Click to try pre-defined examples
- **Error handling** - Clear error messages for invalid inputs
- **Modern design** - Responsive and user-friendly interface
- **Real-time feedback** - Immediate calculation results

## Testing

The implementation includes comprehensive test coverage:
- Basic calculations
- Custom delimiters
- Newline separators
- Negative number validation
- Edge cases
- Invalid inputs

Run tests with:
```bash
python3 tests/test_runner.py
```

## Requirements

- Python 3.6+
- pip3
- Modern web browser (for UI)

## License

This project is part of the Incubyte TDD Assessment.
