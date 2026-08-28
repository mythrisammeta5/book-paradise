# Book Paradise Setup and Run Script for PowerShell
# This script sets up and runs the complete Book Paradise application

# Color output functions
function Write-Success {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Green
}

function Write-Error-Custom {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host $Message -ForegroundColor Cyan
}

# Main execution
Write-Info "=========================================="
Write-Info "Book Paradise - Full Stack Application"
Write-Info "Setup and Installation Script"
Write-Info "=========================================="
Write-Host ""

# Step 1: Check if Python is installed
Write-Info "Step 1: Checking Python installation..."
try {
    $pythonVersion = python --version 2>&1
    Write-Success "✓ Python found: $pythonVersion"
} catch {
    Write-Error-Custom "✗ Python not found. Please install Python 3.8+ from https://www.python.org"
    exit 1
}

# Step 2: Create virtual environment
Write-Info "Step 2: Creating virtual environment..."
if (-Not (Test-Path "venv")) {
    python -m venv venv
    Write-Success "✓ Virtual environment created"
} else {
    Write-Success "✓ Virtual environment already exists"
}

# Step 3: Activate virtual environment
Write-Info "Step 3: Activating virtual environment..."
& ".\venv\Scripts\Activate.ps1"
Write-Success "✓ Virtual environment activated"

# Step 4: Upgrade pip
Write-Info "Step 4: Upgrading pip..."
python -m pip install --upgrade pip
Write-Success "✓ pip upgraded"

# Step 5: Install dependencies
Write-Info "Step 5: Installing dependencies from requirements.txt..."
pip install -r requirements.txt
Write-Success "✓ Dependencies installed"

# Step 6: Create .env file if it doesn't exist
Write-Info "Step 6: Setting up environment variables..."
if (-Not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Success "✓ .env file created from .env.example"
} else {
    Write-Success "✓ .env file already exists"
}

# Step 7: Create instance directory
Write-Info "Step 7: Creating instance directory..."
if (-Not (Test-Path "instance")) {
    New-Item -ItemType Directory -Path "instance" | Out-Null
    Write-Success "✓ instance directory created"
} else {
    Write-Success "✓ instance directory already exists"
}

# Step 8: Initialize database
Write-Info "Step 8: Initializing database..."
python -c "
from app import create_app
app = create_app()
with app.app_context():
    print('Database initialized successfully!')
"
Write-Success "✓ Database initialized with seed data"

# Step 9: Display startup information
Write-Host ""
Write-Info "=========================================="
Write-Info "Setup Complete!"
Write-Info "=========================================="
Write-Host ""
Write-Success "Book Paradise Application is ready to run!"
Write-Host ""
Write-Info "📚 Book Paradise Features:"
Write-Host "  ✓ Book Discovery & Search"
Write-Host "  ✓ Book Rental System"
Write-Host "  ✓ Personal Library Management"
Write-Host "  ✓ Study in Library (Seat Booking)"
Write-Host "  ✓ Home Delivery"
Write-Host "  ✓ Rewards & Achievements"
Write-Host "  ✓ Reading Games (Quiz, Rapid Fire, Memory Match)"
Write-Host "  ✓ AI Reading Assistant"
Write-Host "  ✓ Invoice/Bill Generation"
Write-Host "  ✓ User Profiles & Reviews"
Write-Host ""

# Step 10: Start the application
Write-Info "=========================================="
Write-Info "Starting Book Paradise Application..."
Write-Info "=========================================="
Write-Host ""
Write-Info "🌐 The application will start on: http://localhost:5000"
Write-Host ""
Write-Info "Test Credentials:"
Write-Host "  Username: testuser"
Write-Host "  Password: password123"
Write-Host ""
Write-Info "Press Ctrl+C to stop the server"
Write-Host ""

# Run Flask application
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"

python run.py

# Deactivate virtual environment when done
deactivate
