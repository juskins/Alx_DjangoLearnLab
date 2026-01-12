# Delete Operation

## Command

```python
from bookshelf.models import Book

book.delete()
all_books = Book.objects.all()
print(f"All books after deletion: {list(all_books)}")
```

## Output

```
(1, {'bookshelf.Book': 1})
All books after deletion: [<Book: Book object (1)>]
```

## Description

Successfully deleted the Book instance with ID 2 (title: "Nineteen Eighty-Four").

The deletion process:
1. **Delete the object**: Call `book.delete()` which removes the object from the database
2. **Verify deletion**: Query all books using `Book.objects.all()` to confirm removal

The `delete()` method returns a tuple:
- **First element**: Total number of objects deleted (1)
- **Second element**: Dictionary showing deletions by model type (`{'bookshelf.Book': 1}`)

After deletion, querying all books shows only the previously existing book with ID 1. The book we created (ID 2) has been successfully removed from the database.

Note: Once deleted, the object can no longer be used. Attempting to access or save it will raise an error.
