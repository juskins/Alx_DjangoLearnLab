# API Project - Django REST Framework

## Overview
This is a Django REST Framework project designed for API development. The project includes a simple `Book` model to demonstrate basic API functionality.

## Project Structure
```
api_project/
├── api/                    # Django app for API logic
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py           # Admin registration
│   ├── apps.py
│   ├── models.py          # Book model definition
│   ├── tests.py
│   └── views.py
├── api_project/           # Project settings
│   ├── __init__.py
│   ├── settings.py        # Django settings with DRF installed
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
```

## Setup Instructions

### 1. Prerequisites
- Python 3.x installed
- Django installed: `pip install django`
- Django REST Framework installed: `pip install djangorestframework`

### 2. Project Creation
The project was created using:
```bash
django-admin startproject api_project
cd api_project
python manage.py startapp api
```

### 3. Configuration
- Added `'rest_framework'` and `'api'` to `INSTALLED_APPS` in `settings.py`

### 4. Models
The `Book` model is defined in `api/models.py`:
```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
```

### 5. Database Setup
Migrations were created and applied:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Server
Start the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to confirm the server is running.

## Admin Panel
The Book model is registered in the admin panel. To access it:
1. Create a superuser: `python manage.py createsuperuser`
2. Visit http://127.0.0.1:8000/admin/
3. Login with your credentials

## Features
- ✅ Django REST Framework installed and configured
- ✅ Book model with title and author fields
- ✅ Database migrations applied
- ✅ Admin panel configuration
- ✅ Development server running

## Next Steps
- Create serializers for the Book model
- Implement API views (ListAPIView, DetailAPIView)
- Configure URL routing for API endpoints
- Add authentication and permissions
