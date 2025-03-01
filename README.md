# Animal Shelter Management System

A comprehensive Content Management System (CMS) for animal shelters and charities, built with Django 4.2.18.

## Features

- Complete animal lifecycle management (induction through adoption)
- Animal status tracking (Available, Reserved, Quarantine, Adopted)
- Medical records and treatment tracking
- Cage and building management
- Allergy and medication tracking
- Export functionality (XLS format)
- Role-based access control
- Secure authentication system

## Prerequisites

- Python 3.8+
- PostgreSQL/MySQL
- Redis (for Celery tasks)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/import-tao/shelter-record-manager.git
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

4. Set up the database:
```bash
python manage.py migrate --settings=shelter.settings.base_settings
python manage.py createsuperuser --settings=shelter.settings.base_settings
```

5. Run the development server:
```bash
python manage.py runserver --settings=shelter.settings.base_settings
```

## Development

1. Install development dependencies:
```bash
pip install -r requirements/requirements_local.txt
```

2. Run tests:
```bash
python manage.py test --settings=shelter.settings.base_settings
```

## Key Dependencies

- Django==4.2.18
- django-crispy-forms==2.1
- django-import-export==3.3.7
- djangorestframework==3.15.2
- gunicorn==22.0.0
- Pillow==11.1.0
- celery==5.5.0b1
- redis==5.0.1

## Security Features

- HTTPS enforcement
- Secure authentication
- XSS protection
- SQL injection protection
- Request smuggling protection
- Login required for sensitive operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository.