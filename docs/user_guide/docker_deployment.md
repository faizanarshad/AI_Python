# 🐳 Docker Deployment Guide

This guide will help you deploy the AI-Powered E-commerce Analytics Hub using Docker for professional, scalable deployment.

## 📋 Prerequisites

- **Docker** (version 20.10 or higher)
- **Docker Compose** (version 2.0 or higher)
- **Git** (for cloning the repository)

### Installing Docker

#### macOS
```bash
# Install Docker Desktop
brew install --cask docker
```

#### Ubuntu/Debian
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### Windows
Download and install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop).

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd AI_Python
```

### 2. Build and Run (Production)
```bash
# Build the Docker image
make docker-build

# Run the production container
make docker-run
```

### 3. Access the Dashboard
Open your browser and navigate to:
- **Local**: http://localhost:8501
- **Network**: http://your-ip:8501

## 🔧 Development Mode

### Run Development Container
```bash
# Build and run development container with hot reload
make docker-dev
```

### Access Development Dashboard
- **Local**: http://localhost:8502
- **Network**: http://your-ip:8502

## 🐳 Docker Commands

### Basic Commands

```bash
# Build Docker image
make docker-build

# Run production container
make docker-run

# Run development container
make docker-dev

# Stop all containers
make docker-stop

# View logs
make docker-logs

# Clean up Docker resources
make docker-clean
```

### Manual Docker Commands

```bash
# Build image
docker build -t ai-ecommerce-dashboard:latest .

# Run container
docker run -d -p 8501:8501 --name dashboard ai-ecommerce-dashboard:latest

# Run with volume mounts
docker run -d -p 8501:8501 \
  -v $(pwd)/assets/data:/app/assets/data:ro \
  -v $(pwd)/logs:/app/logs \
  --name dashboard ai-ecommerce-dashboard:latest

# View logs
docker logs -f dashboard

# Stop container
docker stop dashboard

# Remove container
docker rm dashboard
```

## 🏭 Production Deployment

### Using Docker Compose

```bash
# Start production stack with Nginx
make docker-prod

# Or manually
docker-compose --profile production up -d
```

### Environment Configuration

Create a `.env` file for production settings:

```bash
# .env
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### SSL/HTTPS Setup

1. **Generate SSL certificates**:
```bash
mkdir -p nginx/ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout nginx/ssl/key.pem \
  -out nginx/ssl/cert.pem
```

2. **Update nginx configuration**:
   - Uncomment the HTTPS server block in `nginx/nginx.conf`
   - Update the server name to your domain

3. **Run with SSL**:
```bash
docker-compose --profile production up -d
```

## 📊 Monitoring and Logs

### View Application Logs
```bash
# Streamlit logs
docker-compose logs -f dashboard

# Nginx logs (if using production profile)
docker-compose logs -f nginx
```

### Health Checks
```bash
# Check container health
docker ps

# Test health endpoint
curl http://localhost/health
```

### Resource Monitoring
```bash
# View container stats
docker stats

# View resource usage
docker system df
```

## 🔒 Security Considerations

### Production Security Checklist

- [ ] **Use non-root user** (already configured in Dockerfile)
- [ ] **Enable HTTPS** with valid SSL certificates
- [ ] **Set up firewall rules** to restrict access
- [ ] **Use secrets management** for sensitive data
- [ ] **Regular security updates** of base images
- [ ] **Monitor logs** for suspicious activity

### Security Headers

The Nginx configuration includes security headers:
- `X-Frame-Options`: Prevents clickjacking
- `X-XSS-Protection`: XSS protection
- `X-Content-Type-Options`: Prevents MIME sniffing
- `Content-Security-Policy`: Content security policy

## 📈 Scaling and Performance

### Horizontal Scaling
```bash
# Scale to multiple instances
docker-compose up -d --scale dashboard=3
```

### Load Balancing
The Nginx configuration includes load balancing capabilities:
```nginx
upstream streamlit {
    server dashboard:8501;
    server dashboard2:8501;
    server dashboard3:8501;
}
```

### Performance Optimization

1. **Resource Limits**:
```yaml
# docker-compose.yml
services:
  dashboard:
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 2G
        reservations:
          cpus: '1.0'
          memory: 1G
```

2. **Caching**:
   - Enable Redis for session caching
   - Use CDN for static assets
   - Implement browser caching

## 🚨 Troubleshooting

### Common Issues

#### Container Won't Start
```bash
# Check logs
docker-compose logs dashboard

# Check if port is available
netstat -tulpn | grep 8501

# Restart container
docker-compose restart dashboard
```

#### Data Not Loading
```bash
# Check if data files are mounted
docker exec -it dashboard ls -la assets/data/

# Check file permissions
docker exec -it dashboard ls -la assets/data/Dataset.csv
```

#### Performance Issues
```bash
# Check resource usage
docker stats

# Increase memory limit
docker-compose down
docker-compose up -d --scale dashboard=1
```

### Debug Mode
```bash
# Run in debug mode
docker run -it --rm -p 8501:8501 \
  -v $(pwd):/app \
  ai-ecommerce-dashboard:latest bash
```

## 🔄 CI/CD Integration

### GitHub Actions Example
```yaml
# .github/workflows/docker-deploy.yml
name: Docker Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build Docker image
        run: docker build -t ai-ecommerce-dashboard:${{ github.sha }} .
      
      - name: Deploy to server
        run: |
          # Add your deployment commands here
          docker-compose pull
          docker-compose up -d
```

## 📚 Advanced Configuration

### Custom Dockerfile
```dockerfile
# Dockerfile.custom
FROM ai-ecommerce-dashboard:latest

# Add custom configurations
COPY custom_config.py /app/src/config/
COPY custom_assets /app/assets/

# Install additional packages
RUN pip install additional-package
```

### Multi-stage Build
```dockerfile
# Dockerfile.multistage
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.9-slim
COPY --from=builder /root/.local /root/.local
# ... rest of configuration
```

## 🎉 Success!

Your AI-Powered E-commerce Analytics Hub is now running in a professional Docker environment! 

### Next Steps:
1. **Monitor performance** using the provided tools
2. **Set up automated backups** for your data
3. **Configure monitoring** (Prometheus, Grafana)
4. **Set up alerts** for critical issues
5. **Plan for scaling** as your user base grows

Happy deploying! 🚀🐳 