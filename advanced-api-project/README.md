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

-   `GET /api/authors/`: List all authors and their books.
-   `POST /api/authors/`: Create a new author.
-   `GET /api/authors/<id>/`: Retrieve a specific author.
-   `PUT /api/authors/<id>/`: Update an author.
-   `DELETE /api/authors/<id>/`: Remove an author.
-   `GET /api/books/`: List all books.
-   `POST /api/books/`: Create a new book.
-   `GET /api/books/<id>/`: Retrieve a specific book.
-   `PUT /api/books/<id>/`: Update a book.
-   `DELETE /api/books/<id>/`: Remove a book.

## Features

-   **Models**: `Author` and `Book` with a one-to-many relationship.
-   **Serializers**:
    -   `BookSerializer`: Includes custom validation to prevent future publication years.
    -   `AuthorSerializer`: Includes nested `BookSerializer` to list related books.
-   **Views**: Generic API views for boilerplate-free CRUD operations.
