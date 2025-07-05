#!/bin/bash

# 🚀 AI-Powered E-commerce Analytics Hub - Docker Setup Script
# Quick setup and deployment automation

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
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

print_header() {
    echo -e "${PURPLE}================================${NC}"
    echo -e "${PURPLE}🚀 AI E-commerce Analytics Hub${NC}"
    echo -e "${PURPLE}🐳 Docker Setup & Deployment${NC}"
    echo -e "${PURPLE}================================${NC}"
    echo ""
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check Docker installation
check_docker() {
    print_status "Checking Docker installation..."
    
    if ! command_exists docker; then
        print_error "Docker is not installed. Please install Docker first."
        echo "Visit: https://docs.docker.com/get-docker/"
        exit 1
    fi
    
    if ! command_exists docker-compose; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        echo "Visit: https://docs.docker.com/compose/install/"
        exit 1
    fi
    
    # Check if Docker daemon is running
    if ! docker info >/dev/null 2>&1; then
        print_error "Docker daemon is not running. Please start Docker."
        exit 1
    fi
    
    print_success "Docker and Docker Compose are properly installed and running!"
}

# Function to check data files
check_data_files() {
    print_status "Checking data files..."
    
    if [ ! -f "assets/data/Dataset.csv" ]; then
        print_warning "Dataset.csv not found in assets/data/"
        print_status "Please ensure your data file is in the correct location."
        return 1
    fi
    
    print_success "Data files found!"
    return 0
}

# Function to build Docker image
build_image() {
    print_status "Building Docker image..."
    
    if docker build -t ai-ecommerce-dashboard:latest .; then
        print_success "Docker image built successfully!"
    else
        print_error "Failed to build Docker image."
        exit 1
    fi
}

# Function to run production container
run_production() {
    print_status "Starting production container..."
    
    if docker-compose up -d dashboard; then
        print_success "Production container started successfully!"
        echo ""
        echo -e "${CYAN}🌐 Access your dashboard at:${NC}"
        echo -e "${GREEN}   Local:  http://localhost:8501${NC}"
        echo -e "${GREEN}   Network: http://$(hostname -I | awk '{print $1}'):8501${NC}"
        echo ""
        echo -e "${YELLOW}📋 Useful commands:${NC}"
        echo -e "   View logs: ${CYAN}docker-compose logs -f dashboard${NC}"
        echo -e "   Stop:      ${CYAN}docker-compose down${NC}"
        echo -e "   Restart:   ${CYAN}docker-compose restart dashboard${NC}"
    else
        print_error "Failed to start production container."
        exit 1
    fi
}

# Function to run development container
run_development() {
    print_status "Starting development container..."
    
    if docker-compose --profile dev up -d dashboard-dev; then
        print_success "Development container started successfully!"
        echo ""
        echo -e "${CYAN}🌐 Access your development dashboard at:${NC}"
        echo -e "${GREEN}   Local:  http://localhost:8502${NC}"
        echo -e "${GREEN}   Network: http://$(hostname -I | awk '{print $1}'):8502${NC}"
        echo ""
        echo -e "${YELLOW}📋 Development features:${NC}"
        echo -e "   ✅ Hot reload enabled"
        echo -e "   ✅ Source code mounted"
        echo -e "   ✅ Development tools included"
        echo ""
        echo -e "${YELLOW}📋 Useful commands:${NC}"
        echo -e "   View logs: ${CYAN}docker-compose logs -f dashboard-dev${NC}"
        echo -e "   Stop:      ${CYAN}docker-compose down${NC}"
        echo -e "   Restart:   ${CYAN}docker-compose restart dashboard-dev${NC}"
    else
        print_error "Failed to start development container."
        exit 1
    fi
}

# Function to run production stack with Nginx
run_production_stack() {
    print_status "Starting production stack with Nginx..."
    
    if docker-compose --profile production up -d; then
        print_success "Production stack started successfully!"
        echo ""
        echo -e "${CYAN}🌐 Access your dashboard at:${NC}"
        echo -e "${GREEN}   Local:  http://localhost${NC}"
        echo -e "${GREEN}   Network: http://$(hostname -I | awk '{print $1}')${NC}"
        echo ""
        echo -e "${YELLOW}📋 Stack components:${NC}"
        echo -e "   ✅ Dashboard application"
        echo -e "   ✅ Nginx reverse proxy"
        echo -e "   ✅ Load balancing ready"
        echo -e "   ✅ SSL/HTTPS ready"
        echo ""
        echo -e "${YELLOW}📋 Useful commands:${NC}"
        echo -e "   View logs: ${CYAN}docker-compose logs -f${NC}"
        echo -e "   Stop:      ${CYAN}docker-compose down${NC}"
        echo -e "   Restart:   ${CYAN}docker-compose restart${NC}"
    else
        print_error "Failed to start production stack."
        exit 1
    fi
}

# Function to show status
show_status() {
    print_status "Checking container status..."
    
    echo ""
    echo -e "${CYAN}📊 Container Status:${NC}"
    docker-compose ps
    
    echo ""
    echo -e "${CYAN}📊 Docker Images:${NC}"
    docker images | grep ai-ecommerce-dashboard
    
    echo ""
    echo -e "${CYAN}📊 Resource Usage:${NC}"
    docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
}

# Function to clean up
cleanup() {
    print_status "Cleaning up Docker resources..."
    
    docker-compose down --rmi all --volumes --remove-orphans
    docker system prune -f
    
    print_success "Cleanup completed!"
}

# Function to show help
show_help() {
    echo ""
    echo -e "${CYAN}Usage: $0 [OPTION]${NC}"
    echo ""
    echo -e "${YELLOW}Options:${NC}"
    echo -e "  ${GREEN}build${NC}      - Build Docker image"
    echo -e "  ${GREEN}run${NC}        - Run production container"
    echo -e "  ${GREEN}dev${NC}        - Run development container"
    echo -e "  ${GREEN}prod${NC}       - Run production stack with Nginx"
    echo -e "  ${GREEN}status${NC}     - Show container status"
    echo -e "  ${GREEN}cleanup${NC}    - Clean up Docker resources"
    echo -e "  ${GREEN}check${NC}      - Check prerequisites"
    echo -e "  ${GREEN}help${NC}       - Show this help message"
    echo ""
    echo -e "${YELLOW}Examples:${NC}"
    echo -e "  ${CYAN}$0 build${NC}    - Build the Docker image"
    echo -e "  ${CYAN}$0 run${NC}      - Start production container"
    echo -e "  ${CYAN}$0 dev${NC}      - Start development container"
    echo -e "  ${CYAN}$0 prod${NC}     - Start full production stack"
    echo ""
}

# Main script logic
main() {
    print_header
    
    case "${1:-help}" in
        "build")
            check_docker
            check_data_files
            build_image
            ;;
        "run")
            check_docker
            check_data_files
            build_image
            run_production
            ;;
        "dev")
            check_docker
            check_data_files
            build_image
            run_development
            ;;
        "prod")
            check_docker
            check_data_files
            build_image
            run_production_stack
            ;;
        "status")
            check_docker
            show_status
            ;;
        "cleanup")
            check_docker
            cleanup
            ;;
        "check")
            check_docker
            check_data_files
            print_success "All prerequisites are met!"
            ;;
        "help"|*)
            show_help
            ;;
    esac
}

# Run main function with all arguments
main "$@" 