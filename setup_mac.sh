#!/bin/bash

echo "🧠 Setting up CuckBayes on macOS..."

# Ensure Homebrew is available
if ! command -v brew &>/dev/null; then
    echo "❌ Homebrew not found. Please install Homebrew first: https://brew.sh/"
    exit 1
fi

# Install Python 3.11 if needed
if ! command -v python3.11 &>/dev/null; then
    echo "📦 Installing Python 3.11 via Homebrew..."
    brew install python@3.11
    brew link python@3.11 --force
else
    echo "✅ Python 3.11 is already installed."
fi

# Create virtual environment
echo "📁 Creating virtual environment..."
python3.11 -m venv venv

# Activate environment
echo "🐍 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    echo "📦 Installing Python dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ requirements.txt not found — installing minimal packages manually..."
    pip install rich InquirerPy pygame Pillow
fi

echo "✅ Setup complete. Run the app with: source venv/bin/activate && python cuckbayes_cli.py"
