# Django Relationship App - Views Implementation

## Overview
This document describes the implementation of function-based and class-based views in the `relationship_app` for displaying books and library information.

## Implementation Details

### Models
The app includes four models with different relationship types:
- **Author**: Stores author information
- **Book**: Has a ForeignKey relationship to Author
- **Library**: Has a ManyToMany relationship to Books
- **Librarian**: Has a OneToOne relationship to Library

### Views Implemented

#### 1. Function-Based View: `list_books`
- **File**: `relationship_app/views.py`
- **Purpose**: Lists all books in the database
- **URL**: `/relationship/books/`
- **Template**: `relationship_app/list_books.html`
- **Implementation**:
  ```python
  def list_books(request):
      books = Book.objects.all()
      return render(request, 'relationship_app/list_books.html', {'books': books})
  ```

#### 2. Class-Based View: `LibraryDetailView`
- **File**: `relationship_app/views.py`
- **Type**: DetailView
- **Purpose**: Displays details of a specific library and all its books
- **URL**: `/relationship/library/<id>/`
- **Template**: `relationship_app/library_detail.html`
- **Implementation**:
  ```python
  class LibraryDetailView(DetailView):
      model = Library
      template_name = 'relationship_app/library_detail.html'
      context_object_name = 'library'
  ```

### URL Configuration

**File**: `relationship_app/urls.py`
```python
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
```

**Main Project URLs**: `django_models/urls.py`
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),
]
```

### Templates

#### list_books.html
Displays all books with their titles and authors in an unordered list.

#### library_detail.html
Shows library name and all books in that library with author and publication year.

## Testing the Application

### Access the Views

1. **List all books**:
   - URL: http://localhost:8000/relationship/books/
   - Displays all books with their authors

2. **View library details**:
   - URL: http://localhost:8000/relationship/library/1/
   - URL: http://localhost:8000/relationship/library/2/
   - URL: http://localhost:8000/relationship/library/3/
   - Displays specific library details with all books

### Sample Data
The database has been populated with:
- 4 Authors (J.K. Rowling, George R.R. Martin, J.R.R. Tolkien, Agatha Christie)
- 8 Books
- 3 Libraries (Central City Library, University Library, Community Library)
- 3 Librarians

### Running the Server
```bash
python manage.py runserver
```

### Admin Panel
Access the admin panel at http://localhost:8000/admin/ to manage the data.

## Files Modified/Created

1. **Models**: `relationship_app/models.py`
2. **Views**: `relationship_app/views.py`
3. **URLs**: `relationship_app/urls.py`
4. **Admin**: `relationship_app/admin.py`
5. **Templates**:
   - `relationship_app/templates/relationship_app/list_books.html`
   - `relationship_app/templates/relationship_app/library_detail.html`
6. **Settings**: `django_models/settings.py` (added relationship_app to INSTALLED_APPS)
7. **Main URLs**: `django_models/urls.py` (included relationship_app URLs)

## Key Features

- ✅ Function-based view for listing books
- ✅ Class-based DetailView for library details
- ✅ Proper URL routing for both views
- ✅ HTML templates for structured display
- ✅ Models registered in admin panel
- ✅ Database migrations applied
- ✅ Sample data populated for testing
