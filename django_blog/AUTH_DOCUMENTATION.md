# User Authentication System - Django Blog

This system provides full user lifecycle management, including registration, secure login/logout, and profile updates.

## Features
- **Registration**: Custom signup form extending `UserCreationForm` to include email.
- **Login/Logout**: Built-in Django authentication views configured to use custom templates.
- **Profile Management**: View and update username and email (requires login).

## How it Works
1. **Forms**: `blog/forms.py` contains `CustomUserCreationForm` and `UserUpdateForm`.
2. **Views**:
   - `register`: Handles account creation and redirects to login.
   - `profile`: Uses `@login_required` to restrict access to authenticated users.
   - `LoginView`/`LogoutView`: Django's built-in class-based views.
3. **Templates**: Located in `blog/templates/blog/`, these use Django Template Language and extend `base.html`.
4. **Security**: 
   - Uses CSRF tokens on all POST forms.
   - Leverages Django's pbkdf2 password hashing.
   - Redirects are controlled via `LOGIN_REDIRECT_URL` in `settings.py`.

## Testing Instructions
1. Navigate to `/register/` and create a new account.
2. Log in at `/login/` with your new credentials.
3. Visit `/profile/` to see your details and try updating your email.
4. Log out at `/logout/` and verify you can no longer access the profile page.
