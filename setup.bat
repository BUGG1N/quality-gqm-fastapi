@echo off
REM Setup script for FastAPI GQM Quality Analysis (Windows)
REM This script prepares the environment and runs the complete analysis

echo 🚀 FastAPI GQM Quality Analysis Setup
echo ======================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv .venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo 📚 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Clone FastAPI repository
echo 📥 Cloning FastAPI repository...
if not exist "fastapi" (
    git clone https://github.com/tiangolo/fastapi.git
    cd fastapi
    git checkout 45bfb89ea25fcbe8c44ac5d5657b147cfa074649
    cd ..
) else (
    echo ✅ FastAPI repository already exists
)

echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Activate the environment: .venv\Scripts\Activate.ps1
echo 2. Run analysis: python scripts/collect_all_metrics.py
echo 3. Process results: python scripts/analyze_metrics.py
echo.
echo 📋 Check the docs/ folder for complete reports
echo 📊 Check the data/ folder for raw metrics

pause