# AI-Powered E-commerce Analytics Hub Makefile
# Professional development and deployment automation

.PHONY: help install install-dev clean test lint format docs run run-dev build deploy

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