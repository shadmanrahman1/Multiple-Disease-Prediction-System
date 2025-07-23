# Deployment Guide

This guide covers various deployment options for the Multiple Disease Prediction System.

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- Docker (for containerized deployment)
- GitHub account (for Streamlit Cloud deployment)

## 🚀 Deployment Options

### 1. Local Development Deployment

#### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/Multiple_Disease_prediction.git
cd Multiple_Disease_prediction

# Install dependencies
pip install -r requirements.txt

# Run the application
cd system
streamlit run app.py
```

#### With Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
cd system
streamlit run app.py
```

### 2. Docker Deployment

#### Using Docker
```bash
# Build the image
docker build -t multiple-disease-prediction .

# Run the container
docker run -p 8501:8501 multiple-disease-prediction
```

#### Using Docker Compose
```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

### 3. Streamlit Cloud Deployment

1. **Fork the repository** to your GitHub account

2. **Sign up for Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy the app**
   - Click "New app"
   - Select your repository
   - Set main file path: `system/app.py`
   - Click "Deploy"

4. **Configure secrets** (if needed)
   - Go to app settings
   - Add any required secrets in the secrets management section

### 4. Heroku Deployment

#### Prerequisites
- Heroku CLI installed
- Heroku account

#### Steps
1. **Prepare Heroku files**
   ```bash
   # Create Procfile
   echo "web: streamlit run system/app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   
   # Create runtime.txt
   echo "python-3.9.18" > runtime.txt
   ```

2. **Deploy to Heroku**
   ```bash
   # Login to Heroku
   heroku login
   
   # Create Heroku app
   heroku create your-app-name
   
   # Deploy
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### 5. AWS EC2 Deployment

#### Using EC2 Instance
1. **Launch EC2 instance**
   - Choose Ubuntu 20.04 LTS
   - Configure security groups (port 8501)

2. **Connect and setup**
   ```bash
   # Connect to instance
   ssh -i your-key.pem ubuntu@your-instance-ip
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and Git
   sudo apt install python3 python3-pip git -y
   
   # Clone repository
   git clone https://github.com/yourusername/Multiple_Disease_prediction.git
   cd Multiple_Disease_prediction
   
   # Install dependencies
   pip3 install -r requirements.txt
   
   # Run with nohup for persistent execution
   nohup streamlit run system/app.py --server.port=8501 --server.address=0.0.0.0 &
   ```

### 6. Google Cloud Platform (GCP) Deployment

#### Using Cloud Run
1. **Build and push to Container Registry**
   ```bash
   # Build for GCP
   docker build -t gcr.io/your-project-id/disease-prediction .
   
   # Push to registry
   docker push gcr.io/your-project-id/disease-prediction
   ```

2. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy disease-prediction \
     --image gcr.io/your-project-id/disease-prediction \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

### 7. Azure Container Instances

```bash
# Create resource group
az group create --name disease-prediction-rg --location eastus

# Deploy container
az container create \
  --resource-group disease-prediction-rg \
  --name disease-prediction-app \
  --image your-dockerhub-username/disease-prediction \
  --ports 8501 \
  --dns-name-label disease-prediction-unique
```

## 🔧 Configuration

### Environment Variables
For production deployments, consider setting:
```bash
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### Secrets Management
For sensitive data (if any), use platform-specific secret management:
- **Streamlit Cloud**: App secrets in dashboard
- **Heroku**: Config vars
- **AWS**: Parameter Store or Secrets Manager
- **GCP**: Secret Manager
- **Azure**: Key Vault

## 📊 Monitoring and Logging

### Health Checks
The application includes health check endpoints:
- Streamlit health: `/_stcore/health`
- Custom health check can be added if needed

### Logging
Enable logging for production:
```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Monitoring
Consider adding:
- Application performance monitoring (APM)
- Error tracking (Sentry)
- Uptime monitoring
- Resource usage monitoring

## 🛡️ Security Considerations

### HTTPS
Always use HTTPS in production:
- Streamlit Cloud: HTTPS by default
- Heroku: HTTPS by default
- AWS/GCP/Azure: Configure SSL certificates

### CORS and Security Headers
Configure security headers:
```toml
# .streamlit/config.toml
[server]
enableCORS = false
enableXsrfProtection = true
```

### Input Validation
The app includes input validation, but consider:
- Rate limiting
- Input sanitization
- CSRF protection

## 🔄 CI/CD Pipeline

The repository includes GitHub Actions for:
- Automated testing
- Security scanning
- Docker image building
- Deployment automation

### Automatic Deployment
Configure automatic deployment by:
1. Setting up deployment secrets in GitHub
2. Modifying `.github/workflows/ci-cd.yml`
3. Adding deployment steps for your chosen platform

## 📈 Scaling

### Horizontal Scaling
- Use load balancers
- Deploy multiple instances
- Consider container orchestration (Kubernetes)

### Performance Optimization
- Enable caching: `@st.cache_data`
- Optimize model loading
- Use efficient data structures
- Monitor memory usage

## 🐛 Troubleshooting

### Common Issues
1. **Port conflicts**: Change port in configuration
2. **Memory issues**: Optimize model loading
3. **Package conflicts**: Use virtual environments
4. **File path issues**: Use relative paths

### Debug Mode
Enable debug mode for troubleshooting:
```bash
streamlit run system/app.py --logger.level=debug
```

## 📞 Support

For deployment issues:
1. Check the logs
2. Review this guide
3. Open an issue on GitHub
4. Contact the maintainers

---

Choose the deployment method that best fits your needs and infrastructure requirements!
