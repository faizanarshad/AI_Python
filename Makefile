# AI-Powered E-commerce Analytics Hub Makefile
# Professional development and deployment automation

.PHONY: help install install-dev clean test lint format docs run run-dev build deploy docker-build docker-run docker-dev docker-stop docker-clean docker-logs

# Default target
help:
	@echo "🚀 AI-Powered E-commerce Analytics Hub - Development Commands"
	@echo ""
	@echo "📦 Installation:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo ""
	@echo "🔧 Development:"
	@echo "  run          Run the dashboard in production mode"
	@echo "  run-dev      Run the dashboard in development mode"
	@echo "  clean        Clean build artifacts and cache"
	@echo ""
	@echo "🐳 Docker Commands:"
	@echo "  docker-build Build Docker image"
	@echo "  docker-run   Run production Docker container"
	@echo "  docker-dev   Run development Docker container"
	@echo "  docker-stop  Stop all Docker containers"
	@echo "  docker-clean Clean Docker images and containers"
	@echo "  docker-logs  View Docker container logs"
	@echo ""
	@echo "🧪 Testing & Quality:"
	@echo "  test         Run tests with coverage"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with black and isort"
	@echo "  type-check   Run type checking with mypy"
	@echo ""
	@echo "📚 Documentation:"
	@echo "  docs         Build documentation"
	@echo "  docs-serve   Serve documentation locally"
	@echo ""
	@echo "🚀 Deployment:"
	@echo "  build        Build the package"
	@echo "  deploy       Deploy to production"
	@echo ""
	@echo "📊 Data:"
	@echo "  data-clean   Clean and preprocess data"
	@echo "  data-analyze Run data analysis scripts"

# Installation
install:
	@echo "📦 Installing production dependencies..."
	pip install -e .

install-dev:
	@echo "🔧 Installing development dependencies..."
	pip install -e ".[dev,docs]"
	pre-commit install

# Development
run:
	@echo "🚀 Starting dashboard in production mode..."
	streamlit run app.py --server.port 8501

run-dev:
	@echo "🔧 Starting dashboard in development mode..."
	streamlit run app.py --server.port 8501 --server.headless false

# Docker Commands
docker-build:
	@echo "🐳 Building Docker image..."
	docker build -t ai-ecommerce-dashboard:latest .

docker-run:
	@echo "🚀 Running production Docker container..."
	docker-compose up -d dashboard

docker-dev:
	@echo "🔧 Running development Docker container..."
	docker-compose --profile dev up -d dashboard-dev

docker-stop:
	@echo "🛑 Stopping all Docker containers..."
	docker-compose down

docker-clean:
	@echo "🧹 Cleaning Docker images and containers..."
	docker-compose down --rmi all --volumes --remove-orphans
	docker system prune -f

docker-logs:
	@echo "📋 Viewing Docker container logs..."
	docker-compose logs -f dashboard

docker-prod:
	@echo "🏭 Running production stack with Nginx..."
	docker-compose --profile production up -d

# Cleaning
clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Testing & Quality
test:
	@echo "🧪 Running tests with coverage..."
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

lint:
	@echo "🔍 Running linting checks..."
	flake8 src/ tests/ --max-line-length=88 --extend-ignore=E203,W503
	black --check src/ tests/
	isort --check-only src/ tests/

format:
	@echo "✨ Formatting code..."
	black src/ tests/
	isort src/ tests/

type-check:
	@echo "🔍 Running type checks..."
	mypy src/ --ignore-missing-imports

# Documentation
docs:
	@echo "📚 Building documentation..."
	cd docs && make html

docs-serve:
	@echo "🌐 Serving documentation locally..."
	cd docs/_build/html && python -m http.server 8000

# Deployment
build:
	@echo "🏗️ Building package..."
	python setup.py sdist bdist_wheel

deploy:
	@echo "🚀 Deploying to production..."
	# Add your deployment commands here
	@echo "Deployment completed!"

# Data processing
data-clean:
	@echo "🧹 Cleaning and preprocessing data..."
	python src/utils/data_processing.py

data-analyze:
	@echo "📊 Running data analysis..."
	python src/utils/data_insights.py

# Quick start
quick-start: install-dev run-dev

# Full development setup
setup: install-dev format lint test

# Production deployment
production: clean install build deploy

# Docker quick start
docker-quick: docker-build docker-run
	@echo "✅ Docker container started! Access at http://localhost:8501"

# Full Docker development
docker-full: docker-build docker-dev
	@echo "✅ Development container started! Access at http://localhost:8502" 