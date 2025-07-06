# 🐳 Docker Configuration

This directory contains all Docker-related configuration files for the AI-Powered E-commerce Analytics Hub.

## 📁 Directory Structure

```
docker/
├── production/           # Production Docker configurations
│   └── Dockerfile       # Production Docker image
├── development/          # Development Docker configurations
│   └── Dockerfile       # Development Docker image with hot reload
├── nginx/               # Nginx configurations
│   ├── nginx.conf       # Nginx reverse proxy configuration
│   └── ssl/             # SSL certificates (create as needed)
├── docker-compose.override.yml  # Development overrides
├── docker-compose.prod.yml      # Production configuration
├── .dockerignore        # Docker build exclusions
└── README.md           # This file
```

## 🚀 Quick Start

### Development
```bash
# Run development environment
docker-compose -f docker-compose.yml -f docker/docker-compose.override.yml up

# Or use the script
./scripts/docker-setup.sh dev
```

### Production
```bash
# Run production environment
docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml up

# Or use the script
./scripts/docker-setup.sh prod
```

## 🔧 Configuration Files

### Production Dockerfile
- Optimized for production deployment
- Security best practices
- Health checks enabled
- Non-root user execution

### Development Dockerfile
- Hot reload capabilities
- Development tools included
- Source code mounting
- Debug-friendly configuration

### Nginx Configuration
- Reverse proxy setup
- SSL/HTTPS ready
- Security headers
- Load balancing support
- Rate limiting

## 📊 Environment Variables

### Streamlit Configuration
```bash
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Development Overrides
```bash
STREAMLIT_SERVER_HEADLESS=false
STREAMLIT_SERVER_RUN_ON_SAVE=true
```

## 🔒 Security Features

- Non-root user execution
- Security headers in Nginx
- Rate limiting
- SSL/HTTPS support
- Resource limits

## 📈 Performance Optimization

- Multi-stage builds
- Layer caching
- Resource limits
- Health checks
- Auto-restart policies

## 🛠️ Maintenance

### Build Images
```bash
# Production
docker build -f docker/production/Dockerfile -t ai-ecommerce-dashboard:prod .

# Development
docker build -f docker/development/Dockerfile -t ai-ecommerce-dashboard:dev .
```

### Clean Up
```bash
# Remove all containers and images
docker-compose down --rmi all --volumes --remove-orphans

# Clean Docker system
docker system prune -f
```

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Streamlit Documentation](https://docs.streamlit.io/) 