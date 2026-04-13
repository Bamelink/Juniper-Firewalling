# Juniper Firewall Administration System - Getting Started Guide

## 🎯 What Was Built

A complete Django-based web application for administrating Juniper Firewall Policies and Security Zones with the following components:

### Core Features
- ✅ **Policy Management**: Full CRUD operations for firewall policies
- ✅ **Zone Management**: Create and manage security zones
- ✅ **Address Management**: IP addresses, ranges, and groups
- ✅ **Service Management**: Services with protocol and port definitions
- ✅ **Audit Logging**: Complete change history for all policies
- ✅ **Django Admin Interface**: Built-in admin panel for advanced management
- ✅ **RESTful API Endpoints**: JSON APIs for zones, addresses, and services
- ✅ **PostgreSQL Database**: Robust relational database
- ✅ **Docker Containerization**: Production-ready Docker setup

## 📁 Project Structure

```
Juniper-Firewalling/
├── firewall_admin/           # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Django configuration
│   ├── urls.py              # Main URL routing
│   ├── asgi.py              # ASGI config
│   └── wsgi.py              # WSGI config
│
├── policies/                 # Main Django application
│   ├── models.py            # 5 models: Zone, Address, Service, Policy, PolicyLog
│   ├── views.py             # Views and API endpoints
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin interface configuration
│   ├── urls.py              # App URL routing
│   ├── apps.py              # App configuration
│   ├── __init__.py
│   └── migrations/          # Database migrations
│
├── templates/               # HTML templates
│   ├── base.html            # Base template with navigation
│   ├── index.html           # Dashboard/home page
│   └── policies/
│       ├── policy_list.html
│       ├── policy_detail.html
│       ├── policy_form.html (for create/edit)
│       ├── policy_confirm_delete.html
│       └── zone_list.html
│
├── static/                  # Static files (CSS, JavaScript)
│
├── manage.py                # Django management script
├── Dockerfile               # Docker image definition
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (created at startup)
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore patterns
├── start.sh                 # Docker startup script
├── setup_dev.sh             # Development setup script
└── README.md                # Main documentation
```

## 🚀 Quick Start with Docker (Recommended)

### Step 1: Navigate to Project
```bash
cd /home/kasm-user/Juniper-Firewalling
```

### Step 2: Start the Application
```bash
# Make startup script executable
chmod +x start.sh

# Run the startup script
./start.sh
```

Or manually with Docker Compose:
```bash
docker-compose up -d
```

### Step 3: Access the Application
- **Web Interface**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **Default Credentials**: `admin` / `admin`

### Step 4: View Logs (if needed)
```bash
docker-compose logs -f web
```

## 💻 Local Development Setup

If you prefer local development without Docker:

### Step 1: Setup Virtual Environment
```bash
cd /home/kasm-user/Juniper-Firewalling
chmod +x setup_dev.sh
./setup_dev.sh
```

### Step 2: Install PostgreSQL (if not installed)
```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# macOS
brew install postgresql
```

### Step 3: Create Database
```bash
sudo -u postgres psql
CREATE DATABASE juniper_firewall;
CREATE USER postgres WITH PASSWORD 'postgres';
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET default_transaction_deferrable TO on;
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
GRANT ALL PRIVILEGES ON DATABASE juniper_firewall TO postgres;
\q
```

### Step 4: Run Migrations and Start Server
```bash
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit: http://localhost:8000

## 📊 Database Models

### Zone
Security zones in the firewall
```
- id (PK)
- name (unique)
- description
- created_at, updated_at
```

### Address
IP addresses and address groups
```
- id (PK)
- name (unique)
- address_type (ipv4, ipv4_range, ipv6, ipv6_range, hostname, group)
- value
- description
- created_at, updated_at
```

### Service
Network services
```
- id (PK)
- name (unique)
- protocol (TCP, UDP, ICMP, or both)
- port (1-65535)
- description
- created_at, updated_at
```

### Policy
Firewall policies
```
- id (PK)
- name (unique)
- priority (evaluation order)
- source_zone (FK)
- destination_zone (FK)
- source_addresses (M2M)
- destination_addresses (M2M)
- services (M2M)
- action (allow, deny, reject)
- logging_enabled (boolean)
- enabled (boolean)
- description
- created_at, updated_at
```

### PolicyLog
Audit trail
```
- id (PK)
- policy (FK)
- action (created, updated, deleted, enabled, disabled)
- user
- changes (JSON field)
- timestamp
```

## 🌐 API Endpoints

All endpoints require authentication.

### GET /policies/api/zones/
Returns list of all zones
```json
[
  {"id": 1, "name": "LAN"},
  {"id": 2, "name": "WAN"}
]
```

### GET /policies/api/addresses/
Returns list of all addresses
```json
[
  {
    "id": 1, 
    "name": "Internal_Network",
    "address_type": "ipv4_range",
    "value": "192.168.0.0/16"
  }
]
```

### GET /policies/api/services/
Returns list of all services
```json
[
  {
    "id": 1,
    "name": "HTTP",
    "protocol": "tcp",
    "port": 80
  }
]
```

## 🐳 Docker Commands Reference

### Start Services
```bash
docker-compose up -d
```

### Stop Services
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs -f web      # Web app logs
docker-compose logs -f db       # Database logs
docker-compose logs             # All logs
```

### Rebuild Images
```bash
docker-compose build --no-cache
docker-compose up -d
```

### Run Django Commands
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py shell
```

### Access Database Shell
```bash
docker-compose exec db psql -U postgres -d juniper_firewall
```

### Clean Everything (Warning: Deletes data)
```bash
docker-compose down -v
```

## 📝 Web Interface Features

### Dashboard (Home Page)
- Statistics cards showing policy, zone, address, and service counts
- Quick access to main management sections
- Authentication status

### Policies Page
- List of all firewall policies
- Search by name or description
- Filter by status (enabled/disabled)
- View, edit, delete operations
- Pagination support

### Policy Detail View
- Complete policy information
- Source and destination zones
- Associated addresses and services
- Change history
- Quick edit/delete buttons

### Policy Create/Edit Form
- Form with validation
- Multi-select for addresses and services
- Priority assignment
- Action selection (allow, deny, reject)
- Enable/disable logging
- Enable/disable policy

### Zone Management
- View all zones in card layout
- Create new zones via admin
- Edit zone details
- Delete zones

### Admin Panel
- Full Django admin interface
- Advanced management of all objects
- Bulk operations
- Custom admin filters
- Read-only audit logs

## ⚙️ Environment Configuration

Key environment variables in `.env`:

| Variable | Purpose | Default |
|----------|---------|---------|
| DEBUG | Enable Django debug mode | True |
| SECRET_KEY | Django security key | dev-key |
| ALLOWED_HOSTS | Permitted hostnames | localhost,127.0.0.1 |
| DB_NAME | PostgreSQL database name | juniper_firewall |
| DB_USER | PostgreSQL username | postgres |
| DB_PASSWORD | PostgreSQL password | postgres |
| DB_HOST | Database server | db (or localhost) |
| DB_PORT | Database port | 5432 |
| DJANGO_SUPERUSER_PASSWORD | Admin password | admin |

## 🔒 Security Notes

### Development
- SECRET_KEY should be changed before production
- DEBUG mode is enabled for development
- Default credentials should be changed

### Production
- Set `DEBUG = False`
- Use a strong SECRET_KEY
- Configure ALLOWED_HOSTS properly
- Use environment variables for sensitive data
- Enable HTTPS/SSL
- Configure CSRF middleware
- Use secure session cookies
- Regular security updates

## 🛠️ Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>
```

### Database Connection Error
```bash
# Check if PostgreSQL is running
docker-compose ps

# View database logs
docker-compose logs db
```

### Migrations Not Applied
```bash
# Run migrations manually
docker-compose exec web python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

## 📚 Next Steps

1. **Add Sample Data**:
   - Create zones (LAN, WAN, DMZ, etc.)
   - Add IP addresses and address groups
   - Define services
   - Create policies

2. **Customize Styling**:
   - Modify `templates/base.html`
   - Add custom CSS to `static/` folder
   - Update color scheme and branding

3. **Extend Functionality**:
   - Add policy export (CSV, JSON)
   - Integrate with actual Juniper devices
   - Add policy validation rules
   - Implement policy templates

4. **Deploy to Production**:
   - Set up reverse proxy (Nginx/Apache)
   - Configure SSL certificates
   - Use managed PostgreSQL database
   - Set up monitoring and logging

## 📞 Support

For issues or questions:
1. Check the logs: `docker-compose logs -f web`
2. Review the README.md for detailed documentation
3. Check Django documentation: https://docs.djangoproject.com/
4. Check Docker documentation: https://docs.docker.com/

## ✅ Verification Checklist

After starting the application:

- [ ] Web interface loads at http://localhost:8000
- [ ] Admin panel accessible at http://localhost:8000/admin
- [ ] Can login with default credentials (admin/admin)
- [ ] Database is running (check with `docker-compose ps`)
- [ ] Can create new zones
- [ ] Can create new policies
- [ ] API endpoints return JSON responses
- [ ] Static files are loaded (CSS, JavaScript)

Happy administrating! 🎉
