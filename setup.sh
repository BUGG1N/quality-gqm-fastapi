#!/bin/bash
# Setup script for FastAPI GQM Quality Analysis
# This script prepares the environment and runs the complete analysis

echo "🚀 FastAPI GQM Quality Analysis Setup"
echo "======================================"

# Check if Python is available
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python found: $(python --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv .venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Clone FastAPI repository
echo "📥 Cloning FastAPI repository..."
if [ ! -d "fastapi" ]; then
    git clone https://github.com/tiangolo/fastapi.git
    cd fastapi
    git checkout 45bfb89ea25fcbe8c44ac5d5657b147cfa074649
    cd ..
else
    echo "✅ FastAPI repository already exists"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the environment: source .venv/bin/activate (Linux/Mac) or .venv\\Scripts\\Activate.ps1 (Windows)"
echo "2. Run analysis: python scripts/collect_all_metrics.py"
echo "3. Process results: python scripts/analyze_metrics.py"
echo ""
echo "📋 Check the docs/ folder for complete reports"
echo "📊 Check the data/ folder for raw metrics"