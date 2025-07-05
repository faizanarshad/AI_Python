# 🚀 AI-Powered E-commerce Analytics Hub

A comprehensive, interactive dashboard for analyzing e-commerce consumer behavior with AI adoption insights, built with Streamlit and Plotly.

## 🌟 Features

- **📊 Interactive Analytics**: Advanced charts and visualizations
- **🤖 AI Adoption Analysis**: Deep insights into AI technology adoption
- **👥 Customer Segmentation**: Behavioral and demographic analysis
- **🌍 Geographic Analysis**: Location-based insights
- **💳 Payment Method Analysis**: Transaction behavior patterns
- **📱 Responsive Design**: Modern, mobile-friendly interface
- **🔍 Real-time Filtering**: Dynamic data exploration
- **📥 Data Export**: Download filtered results

## 🐳 Docker Quick Start

### Prerequisites
- Docker (version 20.10+)
- Docker Compose (version 2.0+)

### Quick Deployment
```bash
# Clone the repository
git clone <repository-url>
cd AI_Python

# Build and run with Docker
make docker-quick

# Access the dashboard
open http://localhost:8501
```

### Development Mode
```bash
# Run development container with hot reload
make docker-dev

# Access development dashboard
open http://localhost:8502
```

### Production Deployment
```bash
# Deploy with Nginx reverse proxy
make docker-prod

# Access via Nginx
open http://localhost
```

## 🛠️ Local Development

### Prerequisites
- Python 3.9+
- pip

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd AI_Python

# Install dependencies
make install-dev

# Run the dashboard
make run-dev
```

### Alternative Quick Start
```bash
# One-command setup and run
make quick-start
```

## 📁 Project Structure

```
AI_Python/
├── src/                    # Source code
│   ├── dashboard.py       # Main dashboard application
│   ├── utils/             # Utility modules
│   └── config/            # Configuration files
├── assets/                # Static assets
│   ├── data/             # Data files
│   ├── images/           # Images and icons
│   └── styles/           # CSS styles
├── docs/                 # Documentation
├── examples/             # Example scripts
├── tests/                # Test files
├── Dockerfile            # Production Docker image
├── Dockerfile.dev        # Development Docker image
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
├── Makefile             # Development automation
└── README.md            # This file
```

## 🐳 Docker Commands

| Command | Description |
|---------|-------------|
| `make docker-build` | Build Docker image |
| `make docker-run` | Run production container |
| `make docker-dev` | Run development container |
| `make docker-stop` | Stop all containers |
| `make docker-logs` | View container logs |
| `make docker-clean` | Clean Docker resources |

## 📊 Dashboard Sections

### 1. **Demographics Overview**
- Age distribution analysis
- Gender-based insights
- Income level patterns
- Education background trends

### 2. **AI Adoption Analysis**
- AI technology usage rates
- Adoption barriers and drivers
- Technology preference trends
- Future adoption intentions

### 3. **Payment Method Analysis**
- Payment preference distribution
- Security concerns analysis
- Digital wallet adoption
- Traditional vs modern methods

### 4. **Product Category Analysis**
- Category popularity trends
- Purchase frequency analysis
- Price sensitivity insights
- Seasonal patterns

### 5. **Geographic Analysis**
- Regional adoption patterns
- Country-wise insights
- Urban vs rural trends
- Market penetration analysis

### 6. **Customer Segmentation**
- Behavioral clustering
- Value-based segmentation
- Loyalty analysis
- Engagement patterns

## 🔧 Configuration

### Environment Variables
```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Data Configuration
- Place your CSV data files in `assets/data/`
- Supported formats: CSV, Excel, JSON
- Automatic data validation and cleaning

## 🚀 Deployment Options

### 1. **Docker Deployment** (Recommended)
```bash
# Production deployment
make docker-prod

# Development deployment
make docker-dev
```

### 2. **Local Deployment**
```bash
# Install and run locally
make install-dev
make run-dev
```

### 3. **Cloud Deployment**
- **Heroku**: Use the provided `Procfile`
- **AWS**: Use Docker with ECS/Fargate
- **Google Cloud**: Use Cloud Run
- **Azure**: Use Container Instances

## 📈 Performance Optimization

### Docker Optimizations
- Multi-stage builds for smaller images
- Layer caching for faster builds
- Resource limits and monitoring
- Health checks and auto-restart

### Application Optimizations
- Data caching with Streamlit
- Efficient chart rendering
- Lazy loading for large datasets
- Memory management

## 🔒 Security Features

### Docker Security
- Non-root user execution
- Security headers in Nginx
- Rate limiting and DDoS protection
- Regular security updates

### Application Security
- Input validation and sanitization
- Secure data handling
- CORS configuration
- Environment-based security

## 📚 Documentation

- **[User Guide](docs/user_guide/)** - Complete usage instructions
- **[Docker Guide](docs/user_guide/docker_deployment.md)** - Docker deployment guide
- **[API Reference](docs/api/)** - Technical documentation
- **[Contributing Guide](CONTRIBUTING.md)** - Development guidelines

## 🧪 Testing

```bash
# Run all tests
make test

# Run specific test categories
pytest tests/unit/
pytest tests/integration/

# Run with coverage
pytest --cov=src --cov-report=html
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Set up development environment
make setup

# Run pre-commit hooks
pre-commit install

# Make changes and test
make test
make lint
make format
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit** for the amazing web framework
- **Plotly** for interactive visualizations
- **Pandas** for data manipulation
- **NumPy** for numerical computations

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- **Documentation**: [Project Wiki](https://github.com/your-repo/wiki)

---

**Made with ❤️ for the AI and E-commerce community**

[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-green?logo=python)](https://python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE) 