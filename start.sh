#!/bin/bash
# Startup script for Juniper Firewall Admin

set -e

echo "🔧 Juniper Firewall Administration System"
echo "=========================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Start services
echo "🚀 Starting services..."
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 5

# Check if web service is running
if docker-compose ps web | grep -q "Up"; then
    echo "✅ Services started successfully!"
    echo ""
    echo "📋 Access Information:"
    echo "  Web Interface: http://localhost:8000"
    echo "  Admin Panel: http://localhost:8000/admin"
    echo "  Default Credentials: admin / admin"
    echo ""
    echo "📊 View Logs:"
    echo "  docker-compose logs -f web"
    echo ""
    echo "🛑 Stop Services:"
    echo "  docker-compose down"
else
    echo "❌ Failed to start services. Check logs with:"
    echo "  docker-compose logs"
    exit 1
fi
