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

## Installation and Setup

1.  **Clone the repository** (if applicable).
2.  **Install Django**:
    ```bash
    pip install django
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
*   **Public**: Anyone can view the list of posts and individual post details.
*   **Authentication Required**: Users must be logged in to create a post.
*   **Author Only**: Only the creator of a post has permission to edit or delete it. This is enforced using `UserPassesTestMixin` in the views.

## URL Structure
*   `/`: Post list (Home)
*   `/post/<int:pk>/`: Post detail
*   `/post/new/`: Create a new post
*   `/post/<int:pk>/update/`: Edit a post
*   `/post/<int:pk>/delete/`: Delete a post
*   `/register/`: User registration
*   `/login/`: User login
*   `/logout/`: User logout
*   `/profile/`: User profile
