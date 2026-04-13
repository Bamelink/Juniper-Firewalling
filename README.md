# Juniper Firewall Administration System

A Django-based web application for administrating Juniper Firewall Policies and Security Zones.

## Features

- **Policy Management**: Create, read, update, and delete firewall policies
- **Zone Management**: Define and manage security zones
- **Address Management**: Manage IP addresses and address groups
- **Service Management**: Define services with protocols and ports
- **Audit Logging**: Track changes to policies with user information
- **Django Admin**: Built-in admin interface for advanced management
- **PostgreSQL Database**: Robust database backend
- **Docker Support**: Complete Docker containerization

## Project Structure

```
.
├── firewall_admin/          # Django project configuration
├── policies/                # Main Django app
│   ├── models.py           # Database models (Zone, Address, Service, Policy, PolicyLog)
│   ├── views.py            # Views and API endpoints
│   ├── forms.py            # Django forms
│   ├── admin.py            # Django admin configuration
│   └── urls.py             # URL routing
├── templates/              # HTML templates
│   ├── base.html          # Base template with navigation
│   ├── index.html         # Home page
│   └── policies/          # Policy-related templates
├── static/                # Static files (CSS, JS)
├── manage.py              # Django management script
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Prerequisites

- Docker and Docker Compose (for containerized deployment)
- Python 3.11+ (for local development)
- PostgreSQL (if running without Docker)

## Quick Start with Docker

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Juniper-Firewalling
```

### 2. Configure Environment Variables

Edit `.env` file with your settings:

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Build and Run with Docker Compose

```bash
docker-compose up -d
```

This will:
- Create and start a PostgreSQL database container
- Build and start the Django application container
- Run migrations automatically
- Create a superuser (default: admin/admin)
- Start gunicorn on port 8000

### 4. Access the Application

- **Web Interface**: http://localhost:8000
- **Admin Interface**: http://localhost:8000/admin (admin/admin)
- **API Endpoints**:
  - Zones: http://localhost:8000/policies/api/zones/
  - Addresses: http://localhost:8000/policies/api/addresses/
  - Services: http://localhost:8000/policies/api/services/

## Local Development

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Database

Create a PostgreSQL database:

```bash
createdb juniper_firewall
```

Update `firewall_admin/settings.py` with your database credentials.

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Access at http://localhost:8000

## Database Models

### Zone
Represents a security zone in the firewall
- name (unique)
- description
- created_at, updated_at

### Address
IP addresses, ranges, or address groups
- name (unique)
- address_type (ipv4, ipv4_range, ipv6, ipv6_range, hostname, group)
- value
- description

### Service
Services with protocol and port
- name (unique)
- protocol (TCP, UDP, ICMP, or both)
- port (1-65535)
- description

### Policy
Firewall policies
- name (unique)
- priority (order of evaluation)
- source_zone, destination_zone
- source_addresses, destination_addresses (M2M)
- services (M2M)
- action (allow, deny, reject)
- logging_enabled
- enabled
- description

### PolicyLog
Audit log for all policy changes
- policy (FK)
- action (created, updated, deleted, enabled, disabled)
- user
- changes (JSON)
- timestamp

## API Endpoints

All endpoints require authentication.

### List All Zones
```
GET /policies/api/zones/
```

### List All Addresses
```
GET /policies/api/addresses/
```

### List All Services
```
GET /policies/api/services/
```

## Docker Commands

### View Logs

```bash
docker-compose logs -f web      # Web application logs
docker-compose logs -f db       # Database logs
```

### Stop Services

```bash
docker-compose down
```

### Remove Data (Warning: Deletes database)

```bash
docker-compose down -v
```

### Rebuild Images

```bash
docker-compose build --no-cache
```

### Run Django Management Commands

```bash
docker-compose exec web python manage.py <command>
```

Example - Create superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| DEBUG | True | Django debug mode |
| SECRET_KEY | dev-key | Django secret key (change in production) |
| ALLOWED_HOSTS | localhost,127.0.0.1 | Comma-separated allowed hosts |
| DB_NAME | juniper_firewall | Database name |
| DB_USER | postgres | Database user |
| DB_PASSWORD | postgres | Database password |
| DB_HOST | db | Database host (or localhost) |
| DB_PORT | 5432 | Database port |

## Production Deployment

1. **Update Environment Variables**:
   - Change `SECRET_KEY` to a secure random value
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS` with your domain names

2. **Use a Production Database**:
   - Configure external PostgreSQL instance
   - Use managed database services (AWS RDS, Azure Database, etc.)

3. **Setup Reverse Proxy**:
   - Use Nginx or Apache as reverse proxy
   - Configure SSL/TLS certificates

4. **Security Considerations**:
   - Enable CSRF protection
   - Use secure session cookies
   - Implement proper authentication/authorization
   - Configure firewall rules
   - Keep dependencies updated

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

See LICENSE file for details

## Support

For issues and questions, please open an issue in the repository.
Website to control firewall policies and zones
