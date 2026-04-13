#!/bin/bash
# Quick verification script for the Juniper Firewall Admin setup

echo "🔍 Juniper Firewall Admin - Setup Verification"
echo "=============================================="
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✅${NC} $1"
        return 0
    else
        echo -e "${RED}❌${NC} $1"
        return 1
    fi
}

check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✅${NC} $1/"
        return 0
    else
        echo -e "${RED}❌${NC} $1/"
        return 1
    fi
}

echo "📋 Checking Django Project Files..."
check_file "manage.py"
check_file "firewall_admin/settings.py"
check_file "firewall_admin/urls.py"
check_file "firewall_admin/wsgi.py"
check_file "firewall_admin/asgi.py"

echo ""
echo "📋 Checking Django App (Policies)..."
check_file "policies/models.py"
check_file "policies/views.py"
check_file "policies/forms.py"
check_file "policies/admin.py"
check_file "policies/urls.py"
check_file "policies/apps.py"
check_dir "policies/migrations"

echo ""
echo "📋 Checking Templates..."
check_file "templates/base.html"
check_file "templates/index.html"
check_file "templates/policies/policy_list.html"
check_file "templates/policies/policy_detail.html"
check_file "templates/policies/policy_form.html"
check_file "templates/policies/policy_confirm_delete.html"
check_file "templates/policies/zone_list.html"

echo ""
echo "📋 Checking Docker Configuration..."
check_file "Dockerfile"
check_file "docker-compose.yml"
check_file ".dockerignore"
check_file ".env"
check_file ".env.example"

echo ""
echo "📋 Checking Configuration Files..."
check_file "requirements.txt"
check_file ".gitignore"
check_file "start.sh"
check_file "setup_dev.sh"

echo ""
echo "📋 Checking Documentation..."
check_file "README.md"
check_file "GETTING_STARTED.md"
check_file "SETUP_COMPLETE.md"
check_file "FILES_CREATED.md"

echo ""
echo "📋 Checking Directories..."
check_dir "static"
check_dir "templates"
check_dir "policies"
check_dir "firewall_admin"

echo ""
echo "=============================================="
echo "✅ Setup verification complete!"
echo ""
echo "📚 Documentation:"
echo "  - README.md: Main project documentation"
echo "  - GETTING_STARTED.md: Quick start guide"
echo "  - SETUP_COMPLETE.md: Setup summary"
echo "  - FILES_CREATED.md: Complete file listing"
echo ""
echo "🚀 To start the application:"
echo "  docker-compose up -d"
echo ""
echo "🌐 Access at:"
echo "  Web: http://localhost:8000"
echo "  Admin: http://localhost:8000/admin"
echo "  Credentials: admin / admin"
echo ""
