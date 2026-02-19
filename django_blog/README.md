# Django Blog Project

A comprehensive blogging platform built with Django.

## Features

### 1. User Authentication
*   **Registration**: Users can sign up with an email.
*   **Login/Logout**: Secure session management.
*   **Profile**: Users can view and update their profile information.

### 2. Blog Post Management (CRUD)
*   **List Posts**: View all blog posts.
*   **Post Details**: Read the full content of a post.
*   **Create Post**: Authenticated users can write new posts.
*   **Update Post**: Authors can edit their own posts.
*   **Delete Post**: Authors can remove their own posts.

### 3. Comment System
*   **Add Comments**: Authenticated users can comment on any post directly from the detail page.
*   **View Comments**: All visitors can see comments associated with a post.
*   **Edit/Delete Comments**: Only the author of a comment can update or remove it.

## Installation and Setup

1.  **Clone the repository** (if applicable).
2.  **Install Django**:
    ```bash
    pip install django django-crispy-forms crispy-bootstrap4
    ```
3.  **Run Migrations**:
    ```bash
    python manage.py makemigrations blog
    python manage.py migrate
    ```
4.  **Start the Server**:
    ```bash
    python manage.py runserver
    ```

## Permissions and Access Control
*   **Public**: Anyone can view posts and their comments.
*   **Authentication Required**: Must be logged in to create posts or add comments.
*   **Author Only**: 
    - Only post authors can edit/delete their posts.
    - Only comment authors can edit/delete their comments.
    - Enforced via `UserPassesTestMixin`.

## URL Structure
*   `/`: Post list (Home)
*   `/post/<int:pk>/`: Post detail
*   `/post/new/`: Create a new post
*   `/post/<int:pk>/update/`: Edit a post
*   `/post/<int:pk>/delete/`: Delete a post
*   `/post/<int:pk>/comments/new/`: Add a comment
*   `/comment/<int:pk>/update/`: Edit a comment
*   `/comment/<int:pk>/delete/`: Delete a comment
*   `/register/`: User registration
*   `/login/`: User login
*   `/logout/`: User logout
*   `/profile/`: User profile
