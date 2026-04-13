#!/bin/bash
# Development setup script

echo "🔧 Setting up Juniper Firewall Admin - Development Environment"
echo "=============================================================="

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✨ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
echo "🗄️  Running migrations..."
python manage.py migrate

# Create superuser
echo ""
echo "👤 Creating superuser account..."
python manage.py createsuperuser

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the development server, run:"
echo "   source venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "📖 Then visit: http://localhost:8000"
