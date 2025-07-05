#!/bin/bash

# 🚀 AI-Powered E-commerce Analytics Hub Launcher
# Professional dashboard launcher with error handling and user feedback

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ASCII Art Banner
echo -e "${CYAN}"
cat << "EOF"
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  🚀 AI-Powered E-commerce Analytics Hub                     ║
    ║  Professional Business Intelligence Dashboard               ║
    ║                                                              ║
    ║  Version: 1.0.0                                              ║
    ║  Author: AI Analytics Team                                   ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check Python version
check_python_version() {
    if command_exists python3; then
        PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
        REQUIRED_VERSION="3.8"
        
        if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then
            print_success "Python $PYTHON_VERSION detected (✓)"
            PYTHON_CMD="python3"
        else
            print_error "Python $PYTHON_VERSION detected, but $REQUIRED_VERSION+ is required"
            exit 1
        fi
    elif command_exists python; then
        PYTHON_VERSION=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
        REQUIRED_VERSION="3.8"
        
        if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then
            print_success "Python $PYTHON_VERSION detected (✓)"
            PYTHON_CMD="python"
        else
            print_error "Python $PYTHON_VERSION detected, but $REQUIRED_VERSION+ is required"
            exit 1
        fi
    else
        print_error "Python not found. Please install Python 3.8 or higher."
        exit 1
    fi
}

# Function to check if pip exists
check_pip() {
    if command_exists pip3; then
        PIP_CMD="pip3"
        print_success "pip3 detected (✓)"
    elif command_exists pip; then
        PIP_CMD="pip"
        print_success "pip detected (✓)"
    else
        print_error "pip not found. Please install pip."
        exit 1
    fi
}

# Function to check dependencies
check_dependencies() {
    print_status "Checking dependencies..."
    
    # Check if requirements.txt exists
    if [ ! -f "requirements.txt" ]; then
        print_error "requirements.txt not found in current directory"
        exit 1
    fi
    
    # Check if data file exists
    if [ ! -f "assets/data/Dataset.csv" ]; then
        print_warning "Dataset.csv not found in assets/data/"
        print_warning "Please ensure your data file is in the correct location"
    fi
    
    # Check if main application exists
    if [ ! -f "app.py" ]; then
        print_error "app.py not found in current directory"
        exit 1
    fi
}

# Function to install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    # Check if virtual environment exists
    if [ -d "venv" ] || [ -d ".venv" ]; then
        print_warning "Virtual environment detected. Activating..."
        if [ -d "venv" ]; then
            source venv/bin/activate
        else
            source .venv/bin/activate
        fi
    fi
    
    # Install dependencies
    $PIP_CMD install -r requirements.txt
    
    if [ $? -eq 0 ]; then
        print_success "Dependencies installed successfully (✓)"
    else
        print_error "Failed to install dependencies"
        exit 1
    fi
}

# Function to check if port is available
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; then
        print_warning "Port $port is already in use"
        return 1
    else
        print_success "Port $port is available (✓)"
        return 0
    fi
}

# Function to find available port
find_available_port() {
    local port=8501
    while ! check_port $port; do
        port=$((port + 1))
        if [ $port -gt 8600 ]; then
            print_error "No available ports found in range 8501-8600"
            exit 1
        fi
    done
    echo $port
}

# Function to start dashboard
start_dashboard() {
    local port=$1
    
    print_status "Starting AI-Powered E-commerce Analytics Hub..."
    print_status "Dashboard will be available at: http://localhost:$port"
    print_status "Press Ctrl+C to stop the dashboard"
    echo ""
    
    # Start the dashboard
    $PYTHON_CMD -m streamlit run app.py --server.port $port --server.headless false
}

# Function to show help
show_help() {
    echo -e "${CYAN}Usage: $0 [OPTIONS]${NC}"
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  -p, --port     Specify port number (default: 8501)"
    echo "  -i, --install  Install dependencies before starting"
    echo "  -c, --check    Check dependencies only"
    echo "  -v, --version  Show version information"
    echo ""
    echo "Examples:"
    echo "  $0                    # Start with default settings"
    echo "  $0 -p 8502           # Start on port 8502"
    echo "  $0 -i                # Install dependencies and start"
    echo "  $0 -c                # Check dependencies only"
    echo ""
}

# Function to show version
show_version() {
    echo -e "${CYAN}AI-Powered E-commerce Analytics Hub${NC}"
    echo "Version: 1.0.0"
    echo "Author: AI Analytics Team"
    echo "License: MIT"
    echo ""
}

# Main script logic
main() {
    local port=8501
    local install_deps=false
    local check_only=false
    
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            -v|--version)
                show_version
                exit 0
                ;;
            -p|--port)
                port="$2"
                shift 2
                ;;
            -i|--install)
                install_deps=true
                shift
                ;;
            -c|--check)
                check_only=true
                shift
                ;;
            *)
                print_error "Unknown option: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # Check Python and pip
    check_python_version
    check_pip
    
    # Check dependencies
    check_dependencies
    
    if [ "$check_only" = true ]; then
        print_success "All checks completed successfully!"
        exit 0
    fi
    
    # Install dependencies if requested
    if [ "$install_deps" = true ]; then
        install_dependencies
    fi
    
    # Find available port
    port=$(find_available_port)
    
    # Start dashboard
    start_dashboard $port
}

# Run main function with all arguments
main "$@" 