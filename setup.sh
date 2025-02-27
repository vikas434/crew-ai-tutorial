#!/bin/bash

# Setup script for CrewAI Tutorial
echo "Setting up CrewAI Tutorial development environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please edit .env file with your API keys"
fi

# Create necessary directories if they don't exist
echo "Creating directory structure..."
mkdir -p day1/basic_setup
mkdir -p day2/tools_integration
mkdir -p day3/enhanced_agents
mkdir -p day4/travel_planner

echo "Setup complete!"
echo "Next steps:"
echo "1. Edit .env file with your API keys"
echo "2. Start with day1/basic_setup/README.md" 