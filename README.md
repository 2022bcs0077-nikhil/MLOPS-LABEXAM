# ML OPS Lab Exam - Golla Nikhil (2022BCS0077)

This repository contains a complete ML CI/CD pipeline with automated training, evaluation, and deployment.

## 📋 Project Structure

```
.
├── .github/workflows/
│   └── ml_pipeline.yml          # GitHub Actions CI/CD Workflow
├── train.py                      # Model training script
├── serve.py                      # Flask API for model serving
├── Dockerfile                    # Docker image configuration
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Features

- **Automated Training**: Trains model on every push
- **MSE Comparison**: Compares new model MSE with baseline (BEST_MSE)
- **Conditional Deployment**: Only deploys if model improves
- **Docker Integration**: Builds and pushes Docker image on improvement
- **GitHub Actions**: Complete CI/CD pipeline

## 📊 Workflow Logic

1. **Train Job**: Trains model and extracts MSE from `metrics.json`
2. **Deploy Job**: 
   - If `NEW_MSE < BEST_MSE`: ✅ Build & push Docker image, update BEST_MSE
   - If `NEW_MSE >= BEST_MSE`: ❌ Skip deployment, log comparison result

## 🔧 Setup

### Required GitHub Actions Configuration

**Secrets** (Settings → Secrets and variables → Actions → Secrets):
- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token

**Variables** (Settings → Secrets and variables → Actions → Variables):
- `BEST_MSE`: Initial baseline MSE value (e.g., `1.0`)

**Permissions** (Settings → Actions → General → Workflow permissions):
- Set to "Read and write permissions" to allow updating BEST_MSE variable

## 📝 Usage

```bash
# Clone repository
git clone https://github.com/2022bcs0077-nikhil/MLOPS-LABEXAM.git
cd MLOPS-LABEXAM

# Install dependencies
pip install -r requirements.txt

# Train model locally
python train.py

# Start serving API
python serve.py
```

The workflow automatically triggers on every push to `main` branch.

## 👤 Author
**Golla Nikhil** - 2022BCS0077
