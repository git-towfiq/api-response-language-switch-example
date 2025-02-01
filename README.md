```markdown
# API Response Language Switch Example

A Django REST Framework project demonstrating URL-based language switching for API responses.

## Features
- URL-based language switching (`/en/`, `/fr/`, `/es/`)
- Django built-in translation system
- Translatable API responses
- Language-specific endpoints

## Setup

### 1. System Requirements
Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install gettext python3.13 python3.13-venv
```

### 2. Project Setup
```bash
# Clone repository
git clone <repository-url>
cd django-api-translation

# Create virtual environment
python3.13 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Create 

.env

 file:
```ini
DJANGO_SECRET_KEY='your-secret-key'
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### 4. Translation Setup

Create translation files:
```bash
# Generate message files
python manage.py makemessages -l en
python manage.py makemessages -l fr
python manage.py makemessages -l es

# After editing .po files, compile
python manage.py compilemessages
```

Example translation file (`locale/fr/LC_MESSAGES/django.po`):
```po
msgid "Welcome to our platform"
msgstr "Bienvenue sur notre plateforme"

msgid "Operation successful"
msgstr "Opération réussie"
```

### 5. Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

## API Usage

### Access Endpoints with Language Prefixes

```bash
# English endpoint
curl http://localhost:8000/en/api/v1/example/

# French endpoint
curl http://localhost:8000/fr/api/v1/example/

# Spanish endpoint
curl http://localhost:8000/es/api/v1/example/
```

Example Response:
```json
{
    "success": true,
    "statusCode": 200,
    "message": "Opération réussie",
    "data": {
        "title": "Bienvenue sur notre plateforme"
    }
}
```

## Project Structure
```
django-api-translation/
├── config/
│   ├── settings.py      # Django settings with i18n config
│   └── urls.py          # URL patterns with i18n_patterns
├── apps/
│   └── example_app/
│       ├── api/
│       │   └── v1/
│       │       ├── views.py    # API views with translations
│       │       └── urls.py     # API URLs
│       └── models.py
├── locale/              # Translation files
│   ├── en/
│   ├── fr/
│   └── es/
└── manage.py
```

## Managing Translations

### Add New Language
1. Generate messages:
```bash
python manage.py makemessages -l <lang_code>
```

2. Update settings.py:
```python
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
    ('es', 'Spanish'),
    ('de', 'German'),  # New language
]
```

3. Compile messages:
```bash
python manage.py compilemessages
```

### Development
```bash
python manage.py runserver
```

Visit: http://localhost:8000/en/api/v1/example/

## Contributing
1. Fork repository
2. Create feature branch
3. Submit pull request