# Role-Based Access Control Setup

This guide explains how groups and permissions are configured in this application to restrict access to the `Book` model in the `bookshelf` app.

## Custom Permissions
The `Book` model in `bookshelf/models.py` defines the following custom permissions in its `Meta` class:
- `can_view`: Allows a user to view the list of books.
- `can_create`: Allows a user to add a new book entry.
- `can_edit`: Allows a user to modify an existing book entry.
- `can_delete`: Allows a user to remove a book entry.

## Groups Configuration
The following groups should be created via the Django Admin interface:

1. **Viewers**:
   - Members of this group are assigned the `can_view` permission.
   - They can access the book list view but cannot make any changes.

2. **Editors**:
   - Members of this group are assigned `can_view`, `can_create`, and `can_edit` permissions.
   - They can manage the content of the library but cannot delete entries.

3. **Admins**:
   - Members of this group are assigned all permissions: `can_view`, `can_create`, `can_edit`, and `can_delete`.
   - They have full control over the `Book` model.

## Enforcing Permissions in Views
Access control is enforced in `bookshelf/views.py` using the `@permission_required` decorator. For example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    ...
```
If a user without the required permission attempts to access the view, a `403 Forbidden` response is returned.

## Testing the Setup
1. Create a user for each role (e.g., `test_viewer`, `test_editor`, `test_admin`).
2. Assign each user to their respective group in the Django Admin.
3. Log in as each user and verify they can only perform the actions permitted by their group.
