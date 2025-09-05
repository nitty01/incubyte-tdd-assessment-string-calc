#!/bin/bash

# String Calculator TDD Kata - Cross-Platform Setup and Run Script
# This script sets up the environment and starts the web UI

set -e  # Exit on any error

echo "🚀 String Calculator TDD Kata - Cross-Platform Setup and Run Script"
echo "=================================================================="

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Detect operating system
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        OS="windows"
    else
        OS="unknown"
    fi
    print_status "Detected OS: $OS"
}

# Check if Python 3.12 is installed
check_python() {
    print_status "Checking Python 3.12 installation..."
    
    if command -v python3.12 &> /dev/null; then
        PYTHON_VERSION=$(python3.12 --version 2>&1)
        print_success "Python 3.12 found: $PYTHON_VERSION"
        return 0
    else
        print_warning "Python 3.12 not found"
        return 1
    fi
}

# Install Python 3.12 based on OS
install_python() {
    print_status "Installing Python 3.12..."
    
    case $OS in
        "linux")
            install_python_linux
            ;;
        "macos")
            install_python_macos
            ;;
        "windows")
            install_python_windows
            ;;
        *)
            print_error "Unsupported operating system: $OS"
            print_error "Please install Python 3.12 manually from https://www.python.org/downloads/"
            exit 1
            ;;
    esac
}

# Install Python 3.12 on Linux
install_python_linux() {
    print_status "Installing Python 3.12 on Linux..."
    
    # Check if running as root
    if [[ $EUID -eq 0 ]]; then
        SUDO=""
    else
        SUDO="sudo"
    fi
    
    # Detect Linux distribution
    if command -v apt-get &> /dev/null; then
        # Ubuntu/Debian
        print_status "Detected Ubuntu/Debian, installing Python 3.12..."
        $SUDO apt-get update
        $SUDO apt-get install -y software-properties-common
        $SUDO add-apt-repository -y ppa:deadsnakes/ppa
        $SUDO apt-get update
        $SUDO apt-get install -y python3.12 python3.12-venv python3.12-pip
    elif command -v yum &> /dev/null; then
        # CentOS/RHEL
        print_status "Detected CentOS/RHEL, installing Python 3.12..."
        $SUDO yum install -y epel-release
        $SUDO yum install -y python3.12 python3.12-pip
    elif command -v dnf &> /dev/null; then
        # Fedora
        print_status "Detected Fedora, installing Python 3.12..."
        $SUDO dnf install -y python3.12 python3.12-pip
    elif command -v pacman &> /dev/null; then
        # Arch Linux
        print_status "Detected Arch Linux, installing Python 3.12..."
        $SUDO pacman -S --noconfirm python3.12
    elif command -v zypper &> /dev/null; then
        # openSUSE
        print_status "Detected openSUSE, installing Python 3.12..."
        $SUDO zypper install -y python3.12 python3.12-pip
    else
        print_error "Unsupported Linux distribution"
        print_error "Please install Python 3.12 manually from https://www.python.org/downloads/"
        exit 1
    fi
    
    print_success "Python 3.12 installation completed"
}

# Install Python 3.12 on macOS
install_python_macos() {
    print_status "Installing Python 3.12 on macOS..."
    
    # Check if Homebrew is installed
    if command -v brew &> /dev/null; then
        print_status "Using Homebrew to install Python 3.12..."
        brew install python@3.12
    else
        print_warning "Homebrew not found. Installing Homebrew first..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        print_status "Installing Python 3.12 via Homebrew..."
        brew install python@3.12
    fi
    
    # Create symlink for python3.12
    if ! command -v python3.12 &> /dev/null; then
        print_status "Creating symlink for python3.12..."
        ln -sf /opt/homebrew/bin/python3.12 /usr/local/bin/python3.12 2>/dev/null || true
    fi
    
    print_success "Python 3.12 installation completed"
}

# Install Python 3.12 on Windows
install_python_windows() {
    print_status "Installing Python 3.12 on Windows..."
    
    # Check if Chocolatey is installed
    if command -v choco &> /dev/null; then
        print_status "Using Chocolatey to install Python 3.12..."
        choco install python312 -y
    elif command -v winget &> /dev/null; then
        print_status "Using winget to install Python 3.12..."
        winget install Python.Python.3.12
    else
        print_error "Neither Chocolatey nor winget found on Windows"
        print_error "Please install Python 3.12 manually from https://www.python.org/downloads/"
        print_error "Or install Chocolatey from https://chocolatey.org/install"
        exit 1
    fi
    
    print_success "Python 3.12 installation completed"
}

# Check if pip is installed
check_pip() {
    print_status "Checking pip installation..."
    
    if command -v pip3 &> /dev/null; then
        print_success "pip3 found"
    elif command -v python3.12 -m pip &> /dev/null; then
        print_success "pip found via python3.12 -m pip"
    else
        print_warning "pip not found, installing..."
        case $OS in
            "linux")
                if command -v apt-get &> /dev/null; then
                    $SUDO apt-get install -y python3.12-pip
                elif command -v yum &> /dev/null; then
                    $SUDO yum install -y python3.12-pip
                elif command -v dnf &> /dev/null; then
                    $SUDO dnf install -y python3.12-pip
                fi
                ;;
            "macos")
                python3.12 -m ensurepip --upgrade
                ;;
            "windows")
                python3.12 -m ensurepip --upgrade
                ;;
        esac
        print_success "pip installation completed"
    fi
}

# Create virtual environment if it doesn't exist
setup_venv() {
    print_status "Setting up virtual environment..."
    
    if [ ! -d "venv" ]; then
        print_status "Creating virtual environment with Python 3.12..."
        python3.12 -m venv venv
        print_success "Virtual environment created"
    else
        print_success "Virtual environment already exists"
    fi
    
    # Activate virtual environment
    print_status "Activating virtual environment..."
    if [[ "$OS" == "windows" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi
    print_success "Virtual environment activated"
}

# Install requirements from requirements.txt
install_requirements() {
    print_status "Installing requirements from requirements.txt..."
    
    # Check if requirements.txt exists
    if [ ! -f "requirements.txt" ]; then
        print_error "requirements.txt not found in script directory: $SCRIPT_DIR"
        print_error "Please ensure requirements.txt exists in the same directory as this script"
        exit 1
    fi
    
    # Install packages
    if command -v pip3 &> /dev/null; then
        pip3 install -r requirements.txt
    else
        python3.12 -m pip install -r requirements.txt
    fi
    print_success "Requirements installed from requirements.txt"
}

# Run tests
run_tests() {
    print_status "Running String Calculator tests..."
    
    # Check if test runner exists
    if [ -f "tests/test_runner.py" ]; then
        python3.12 tests/test_runner.py
        print_success "Tests completed"
    else
        print_warning "Test runner not found, skipping tests"
    fi
}

# Start the web UI
start_ui() {
    print_status "Starting String Calculator Web UI..."
    print_success "Web UI will be available at: http://localhost:5000"
    print_status "Press Ctrl+C to stop the server"
    echo ""
    
    # Change to UI directory and start Flask app
    cd ui
    python3.12 app.py
}

# Main execution
main() {
    echo ""
    print_status "Starting setup process..."
    print_status "Script directory: $SCRIPT_DIR"
    echo ""
    
    # Detect OS
    detect_os
    
    # Check and install Python 3.12 if needed
    if ! check_python; then
        print_warning "Python 3.12 not found. Would you like to install it? (y/n)"
        read -p "Install Python 3.12? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            install_python
            # Verify installation
            if ! check_python; then
                print_error "Python 3.12 installation failed or not found in PATH"
                print_error "Please install Python 3.12 manually and try again"
                exit 1
            fi
        else
            print_error "Python 3.12 is required to run this application"
            exit 1
        fi
    fi
    
    # Check pip
    check_pip
    
    # Setup environment
    setup_venv
    install_requirements
    
    echo ""
    print_status "Setup completed successfully!"
    echo ""
    
    # Ask user if they want to run tests
    read -p "Do you want to run tests first? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        run_tests
        echo ""
    fi
    
    # Start the UI
    start_ui
}

# Handle script interruption
trap 'echo -e "\n${YELLOW}Script interrupted. Cleaning up...${NC}"; exit 0' INT

# Run main function
main "$@"
