#!/usr/bin/env python3
"""
String Calculator Web UI
A simple Flask web application for testing the String Calculator implementation.
"""

import sys
import os
from flask import Flask, render_template, request, jsonify

# Add the parent directory to the path to import string_calculator
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from string_calculator.string_calculator import StringCalculator

app = Flask(__name__)
calculator = StringCalculator()

def unescape_string(s):
    """Convert escaped strings like '1\\n2,3' to proper format '1\n2,3'"""
    if not s:
        return s
    
    # Replace common escape sequences
    s = s.replace('\\n', '\n')  # Convert \n to actual newline
    s = s.replace('\\t', '\t')  # Convert \t to actual tab
    s = s.replace('\\r', '\r')  # Convert \r to actual carriage return
    s = s.replace('\\\\', '\\') # Convert \\ to single \
    
    return s

@app.route('/')
def index():
    """Main page with the calculator interface."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """API endpoint to calculate the sum of numbers."""
    try:
        data = request.get_json()
        numbers = data.get('numbers', '')
        
        # Debug: Print the received data
        print("=" * 50)
        print("🔍 DEBUG: Data received for calculation")
        print("=" * 50)
        print(f"Raw JSON data: {data}")
        print(f"Numbers string (before unescape): {repr(numbers)}")
        print(f"Numbers length (before): {len(numbers)}")
        print(f"Characters (before): {[ord(c) for c in numbers]}")
        
        # Unescape the string
        numbers = unescape_string(numbers)
        
        print(f"Numbers string (after unescape): {repr(numbers)}")
        print(f"Numbers length (after): {len(numbers)}")
        print(f"Characters (after): {[ord(c) for c in numbers]}")
        print("=" * 50)
        
        if not numbers:
            print("Empty input detected, returning 0")
            return jsonify({'result': 0, 'error': None})
        
        print(f"Calling calculator.add() with: {repr(numbers)}")
        result = calculator.add(numbers)
        print(f"Calculator returned: {result}")
        print("=" * 50)
        
        return jsonify({'result': result, 'error': None})
        
    except ValueError as e:
        print(f"ValueError caught: {e}")
        return jsonify({'result': None, 'error': str(e)})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({'result': None, 'error': f'Unexpected error: {str(e)}'})

@app.route('/examples')
def examples():
    """Get example calculations for the UI."""
    examples = [
        {
            'input': '',
            'description': 'Empty string',
            'expected': '0'
        },
        {
            'input': '1',
            'description': 'Single number',
            'expected': '1'
        },
        {
            'input': '1,2',
            'description': 'Two numbers',
            'expected': '3'
        },
        {
            'input': '1,2,3,4,5',
            'description': 'Multiple numbers',
            'expected': '15'
        },
        {
            'input': '1\n2,3',
            'description': 'Newline separators',
            'expected': '6'
        },
        {
            'input': '//;\n1;2;3',
            'description': 'Custom delimiter (semicolon)',
            'expected': '6'
        },
        {
            'input': '//[*][%]\n1*2%3',
            'description': 'Multiple custom delimiters',
            'expected': '6'
        },
        {
            'input': '//[***]\n1***2***3',
            'description': 'Arbitrary length delimiter',
            'expected': '6'
        },
        {
            'input': '1001,2,3000',
            'description': 'Large numbers (ignores >1000)',
            'expected': '2'
        },
        {
            'input': '1,-2,3',
            'description': 'Negative numbers (should throw error)',
            'expected': 'Error: negative numbers not allowed: -2'
        }
    ]
    return jsonify(examples)

if __name__ == '__main__':
    print("Starting String Calculator Web UI...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.route('/favicon.ico')
def favicon():
    """Handle favicon requests to avoid 404 errors."""
    return '', 204

@app.route('/get-log/<path:path>')
def handle_get_log(path):
    """Handle any /get-log/* requests to avoid 404 errors."""
    return '', 204
