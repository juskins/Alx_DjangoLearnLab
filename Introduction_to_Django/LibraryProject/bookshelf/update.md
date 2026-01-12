# Update Operation

## Command

```python
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated: ID={book.id}, Title='{book.title}', Author='{book.author}', Year={book.publication_year}")
```

## Output

```
Updated: ID=2, Title='Nineteen Eighty-Four', Author='George Orwell', Year=1949
```

## Description

Successfully updated the book's title from "1984" to "Nineteen Eighty-Four".

The update process involves two steps:
1. **Modify the attribute**: Set `book.title` to the new value
2. **Save to database**: Call `book.save()` to persist the changes

After the update:
- **ID**: 2 (unchanged)
- **Title**: "Nineteen Eighty-Four" (updated)
- **Author**: "George Orwell" (unchanged)
- **Publication Year**: 1949 (unchanged)

Note: Changes to model instances are not saved to the database until you explicitly call the `save()` method.
