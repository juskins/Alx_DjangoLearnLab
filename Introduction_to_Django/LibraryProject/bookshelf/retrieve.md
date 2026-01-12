# Retrieve Operation

## Command

```python
retrieved_book = Book.objects.get(id=book.id)
print(f"Retrieved: ID={retrieved_book.id}, Title='{retrieved_book.title}', Author='{retrieved_book.author}', Year={retrieved_book.publication_year}")
```

## Output

```
Retrieved: ID=2, Title='1984', Author='George Orwell', Year=1949
```

## Description

Successfully retrieved the Book instance from the database using its ID.

The `Book.objects.get()` method retrieves a single object that matches the given parameters. All attributes of the book are accessible:
- **ID**: 2
- **Title**: "1984"
- **Author**: "George Orwell"
- **Publication Year**: 1949

Note: `get()` raises `Book.DoesNotExist` if no matching object is found, or `MultipleObjectsReturned` if more than one object matches the criteria.
