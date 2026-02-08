from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create some test data
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book1 = Book.objects.create(title='Harry Potter 1', publication_year=1997, author=self.author)
        self.book2 = Book.objects.create(title='Harry Potter 2', publication_year=1998, author=self.author)
        
        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})
        self.update_url = lambda pk: reverse('book-update', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse('book-delete', kwargs={'pk': pk})

    def test_list_books(self):
        """Test retrieving the list of books (unauthenticated)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if we have 2 books
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        """Test retrieving a single book's details."""
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter 1')

    def test_create_book_authenticated(self):
        """Test creating a new book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Harry Potter 3',
            'publication_year': 1999,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'Harry Potter 3')

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        data = {'title': 'Secret Book', 'publication_year': 2024, 'author': self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating an existing book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Updated Title', 'publication_year': 1997, 'author': self.author.id}
        response = self.client.put(self.update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        """Test deleting a book as an authenticated user."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filtering(self):
        """Test filtering books by publication year."""
        response = self.client.get(self.list_url, {'publication_year': 1997})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 1')

    def test_searching(self):
        """Test searching for books by title."""
        response = self.client.get(self.list_url, {'search': 'Potter 2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 2')

    def test_ordering(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # book1 (1997) should be before book2 (1998)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 1')
        
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        # book2 (1998) should be before book1 (1997)
        self.assertEqual(response.data[0]['title'], 'Harry Potter 2')

    def test_permission_denied_for_unauthenticated_update(self):
        """Ensure unauthenticated users cannot update books."""
        data = {'title': 'Hack Title', 'publication_year': 2000, 'author': self.author.id}
        response = self.client.put(self.update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
