# Advanced API Project

This project implements a Django REST API for managing Authors and Books.

## Setup Instructions

1.  **Environment Setup**:
    - Ensure Python and Django are installed.
    - Install Django REST Framework: `pip install djangorestframework`.

2.  **Database Migrations**:
    - Run `python manage.py makemigrations api`
    - Run `python manage.py migrate`

3.  **Running the Server**:
    - Start the development server: `python manage.py runserver`

## API Endpoints

### Books
- `GET /api/books/`: List all books. (Open Access)
- `GET /api/books/<int:pk>/`: Retrieve a specific book by ID. (Open Access)
- `POST /api/books/create/`: Add a new book. (Authenticated Users Only)
- `PUT /api/books/update/<int:pk>/`: Update an existing book. (Authenticated Users Only)
- `DELETE /api/books/delete/<int:pk>/`: Delete a book. (Authenticated Users Only)

### Authors
- `GET /api/authors/`: List all authors.
- `GET /api/authors/<int:pk>/`: Retrieve a specific author.

## Features

- **Models**: `Author` and `Book` with a one-to-many relationship.
- **Serializers**:
    - `BookSerializer`: Includes custom validation to prevent future publication years.
    - `AuthorSerializer`: Includes nested `BookSerializer` to list related books.
- **Views**: 
    - Separate generic views for each Book CRUD operation (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`).
    - Custom logic in `perform_create` and `perform_update` for future extensibility.
- **Permissions**:
    - Unauthenticated users have Read-Only access (`GET`).
    - Authenticated users can Create, Update, and Delete.
- **Advanced Querying**:
    - **Filtering**: Filter books by `title`, `author__name`, and `publication_year` using query parameters (e.g., `/api/books/?publication_year=2020`).
    - **Searching**: Search books by `title` and `author__name` (e.g., `/api/books/?search=Django`).
    - **Ordering**: Sort books by `title` or `publication_year` (e.g., `/api/books/?ordering=-publication_year`).

## Testing

The project uses Django's built-in test framework. Tests are located in `api/test_views.py`.

### Running Tests
To run the full test suite, execute:
```bash
python manage.py test api
```

### Test Coverage
- **CRUD Operations**: Verifies creation, retrieval, updates, and deletion of books.
- **Query Parameters**: Validates filtering, searching, and ordering functionality.
- **Permissions**: Ensures only authenticated users can perform write operations while everyone can read.
- **Data Integrity**: Checks that the response data matches the expected model states.
