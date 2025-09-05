# String Calculator - TDD Kata Implementation

A comprehensive implementation of the String Calculator Kata following Test-Driven Development (TDD) principles. This project includes a complete web UI, comprehensive testing suite, and production-ready Docker containerization.

## 🚀 Features

### Core String Calculator
- **Basic Addition**: Handle up to 2 numbers separated by commas
- **Multiple Numbers**: Support for arbitrary number of numbers
- **Newline Separators**: Handle newlines as delimiters (`1\n2,3`)
- **Custom Delimiters**: Support for custom single-character delimiters (`//;\n1;2;3`)
- **Multiple Delimiters**: Support for multiple delimiters (`//[*][%]\n1*2%3`)
- **Arbitrary Length Delimiters**: Support for delimiters of any length (`//[***]\n1***2***3`)
- **Negative Number Validation**: Throws error for negative numbers with clear messages
- **Large Number Filtering**: Ignores numbers greater than 1000
- **Decimal Number Validation**: Rejects decimal numbers with appropriate error messages
- **Input Format Validation**: Validates input format and rejects invalid patterns

### Web UI
- **Modern Interface**: Clean, responsive web interface built with Flask
- **Real-time Calculation**: Instant calculation with visual feedback
- **Error Handling**: Clear error messages displayed in the UI
- **Example Cases**: Interactive examples to test different scenarios
- **Debug Mode**: Detailed logging for troubleshooting

### Testing Suite
- **Comprehensive Tests**: Complete test coverage for all functionality
- **Edge Cases**: Tests for various edge cases and error conditions
- **Custom Delimiters**: Tests for different delimiter scenarios
- **Negative Numbers**: Tests for negative number validation
- **Invalid Inputs**: Tests for various invalid input patterns

### Production Features
- **Docker Support**: Complete Docker containerization with health checks
- **Cross-platform Scripts**: Automated setup and deployment scripts
- **Production Ready**: Optimized for production deployment
- **Security**: Non-root user execution in containers

## 📁 Project Structure

```
incubyte-tdd-assessment-string-calc/
├── string_calculator/           # Core calculator implementation
│   └── string_calculator.py     # Main StringCalculator class
├── ui/                          # Web UI application
│   ├── app.py                   # Flask web application
│   └── templates/
│       └── index.html           # Web UI template
├── tests/                       # Comprehensive test suite
│   ├── test_basic_calculations.py
│   ├── test_custom_delimiters.py
│   ├── test_negative_numbers.py
│   ├── test_newline_delimiters.py
│   ├── test_invalid_inputs.py
│   ├── test_edge_cases.py
│   └── test_runner.py           # Test execution script
├── docs/                        # Documentation
│   └── String+Calculator+Kata+v1.pdf
├── run.sh                       # Main setup and run script
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── docker-compose.yml           # Docker Compose configuration
├── README.md                    # This file
└── .gitignore                   # Git ignore rules
```

## 🛠️ Installation & Setup

### Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd incubyte-tdd-assessment-string-calc

# Run the setup script
chmod +x run.sh
./run.sh
```

### Manual Setup
```bash
# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python tests/test_runner.py

# Start web UI
cd ui
python app.py
```

### Docker Setup
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or run individual container
docker build -t string-calculator .
docker run -p 5000:5000 string-calculator
```

## 🧪 Testing

### Run All Tests
```bash
python tests/test_runner.py
```

### Run Tests with Docker
```bash
# Run tests in container
docker-compose run --rm string-calculator python tests/test_runner.py
```

## 🌐 Web UI Usage

1. **Start the application**:
   ```bash
   ./run.sh
   ```

2. **Open your browser** and navigate to: `http://localhost:5000`

3. **Test different inputs**:
   - Basic: `1,2,3`
   - Newlines: `1\n2,3`
   - Custom delimiters: `//;\n1;2;3`
   - Multiple delimiters: `//[*][%]\n1*2%3`

4. **View examples**: Click on any example in the UI to try it

## 📋 String Calculator Rules

1. **Empty string** returns `0`
2. **Single number** returns the number
3. **Two numbers** returns their sum
4. **Multiple numbers** returns the sum of all
5. **Newline separators** are supported (`1\n2,3`)
6. **Custom delimiters** are supported (`//;\n1;2;3`)
7. **Negative numbers** throw an error with all negatives listed
8. **Numbers > 1000** are ignored
9. **Decimal numbers** are rejected with error message
10. **Invalid formats** are rejected with appropriate error messages

## 🔧 API Endpoints

### POST /calculate
Calculate the sum of numbers from a string input.

**Request:**
```json
{
  "numbers": "1,2,3"
}
```

**Response:**
```json
{
  "result": 6,
  "error": null
}
```

**Error Response:**
```json
{
  "result": null,
  "error": "negative numbers not allowed: -1 -2"
}
```

### GET /examples
Get example calculations for the UI.

## 🐳 Docker Configuration

### Dockerfile Features
- **Python 3.12**: Latest stable Python version
- **Security**: Non-root user execution
- **Health Checks**: Built-in health monitoring
- **Optimized**: Multi-stage build for smaller image size
- **Production Ready**: Configured for production deployment

### Docker Compose Features
- **Service Management**: Easy service orchestration
- **Health Monitoring**: Automatic health checks
- **Volume Mounting**: Persistent log storage
- **Environment Configuration**: Production environment setup
- **Restart Policy**: Automatic restart on failure

## 📊 Performance

- **Fast calculation**: Optimized parsing and calculation algorithms
- **Memory efficient**: Minimal memory footprint
- **Scalable**: Designed for high-throughput scenarios
- **Robust error handling**: Graceful handling of edge cases
- **Container optimized**: Efficient Docker image

## 🚀 Deployment

### Production Deployment
```bash
# Build production image
docker build -t string-calculator:latest .

# Run with production settings
docker run -d \
  --name string-calculator \
  -p 5000:5000 \
  -e FLASK_ENV=production \
  string-calculator:latest
```

### Docker Compose Deployment
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏆 Acknowledgments

- **String Calculator Kata** - Original TDD exercise
- **Test-Driven Development** - Development methodology
- **Flask** - Web framework
- **Python** - Programming language
- **Docker** - Containerization platform

---

**Built with ❤️ using Test-Driven Development principles**
