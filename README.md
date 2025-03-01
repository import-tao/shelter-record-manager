# Animal Shelter Management System

A comprehensive Content Management System (CMS) for animal shelters and charities, built with Django 4.2.

## Features

- Complete animal lifecycle management
- Adoption and fostering workflows
- Medical records and treatment tracking
- Event management and volunteer coordination
- Donation and sponsorship handling
- RESTful API
- Celery for background tasks
- Modern security features

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Redis (for Celery)
- Node.js 16+ (if using React frontend)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shelter-record-manager.git
cd shelter-record-manager
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements/requirements_production.txt
# For development, also install:
pip install -r requirements/requirements_local.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Set up the database:
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Collect static files:
```bash
python manage.py collectstatic
```

7. Start Redis server (required for Celery)

8. Start Celery worker:
```bash
celery -A shelter worker -l info
celery -A shelter beat -l info
```

9. Run the development server:
```bash
python manage.py runserver
```

## Environment Variables

Copy `.env.example` to `.env` and configure the following variables:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_*`: Database configuration
- `EMAIL_*`: Email server configuration
- `CELERY_BROKER_URL`: Redis URL for Celery
- `AWS_*`: AWS S3 configuration (if using S3 for storage)

## Development

1. Install development dependencies:
```bash
pip install -r requirements/requirements_local.txt
```

2. Enable debug toolbar by setting `DEBUG=True` in `.env`

3. Run tests:
```bash
pytest
```

4. Check code quality:
```bash
black .
flake8
mypy .
```

## API Documentation

The API is built using Django REST Framework. Documentation is available at:

- `/api/docs/` - API documentation
- `/api/schema/` - OpenAPI schema

## Security Features

- HTTPS enforcement
- Secure cookie settings
- HSTS enabled
- XSS protection
- Content type nosniff
- X-Frame-Options denial
- CORS configuration

## Deployment

1. Set `DEBUG=False` in production
2. Configure proper database settings
3. Set up proper email backend
4. Configure AWS S3 for media storage
5. Set up proper SSL/TLS certificates
6. Configure proper CORS settings
7. Set up proper backup strategy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django community
- Contributors and maintainers
- Animal shelter staff and volunteers who provided valuable feedback

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.