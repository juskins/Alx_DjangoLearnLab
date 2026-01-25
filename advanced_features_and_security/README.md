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

## Security Measures

Several security measures have been implemented to protect the application:

### 1. Secure Settings
In `settings.py`, the following configurations enhance production security:
- `DEBUG = False`: Disables detailed error pages that could leak sensitive information.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables the browser's XSS filtering.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents the site from being framed, protecting against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents the browser from guessing content types.
- `CSRF_COOKIE_SECURE = True` & `SESSION_COOKIE_SECURE = True`: Ensures cookies are only sent over HTTPS.
- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP traffic to HTTPS.

### 2. Cross-Site Request Forgery (CSRF) Protection
All POST forms in the application, such as the one in `bookshelf/templates/bookshelf/form_example.html`, include the `{% csrf_token %}` tag. This ensures that form submissions are validated against CSRF attacks.

### 3. SQL Injection Prevention
Data access in `bookshelf/views.py` is performed using Django's ORM. Instead of using raw SQL or string formatting, we use:
- `get_object_or_404(Book, pk=pk)`
- `Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))`
These methods use parameterized queries behind the scenes, effectively neutralizing SQL injection risks.

### 4. Content Security Policy (CSP)
A Content Security Policy has been implemented using `django-csp`. This identifies which sources of content are trusted, significantly reducing the risk of XSS attacks.
Configurations include:
- `CSP_DEFAULT_SRC`: Default to `'self'`.
- Specific sources for styles and fonts to allow trusted CDNs (e.g., Google Fonts).
