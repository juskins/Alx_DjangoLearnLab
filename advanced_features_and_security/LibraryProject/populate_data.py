"""
Script to populate the database with sample data for testing.
Run this script with: python manage.py shell < populate_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Clear existing data
print("Clearing existing data...")
Librarian.objects.all().delete()
Library.objects.all().delete()
Book.objects.all().delete()
Author.objects.all().delete()

# Create authors
print("Creating authors...")
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George R.R. Martin")
author3 = Author.objects.create(name="J.R.R. Tolkien")
author4 = Author.objects.create(name="Agatha Christie")

# Create books
print("Creating books...")
book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1, publication_year=1997)
book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1, publication_year=1998)
book3 = Book.objects.create(title="A Game of Thrones", author=author2, publication_year=1996)
book4 = Book.objects.create(title="A Clash of Kings", author=author2, publication_year=1998)
book5 = Book.objects.create(title="The Hobbit", author=author3, publication_year=1937)
book6 = Book.objects.create(title="The Lord of the Rings", author=author3, publication_year=1954)
book7 = Book.objects.create(title="Murder on the Orient Express", author=author4, publication_year=1934)
book8 = Book.objects.create(title="And Then There Were None", author=author4, publication_year=1939)

# Create libraries
print("Creating libraries...")
library1 = Library.objects.create(name="Central City Library")
library2 = Library.objects.create(name="University Library")
library3 = Library.objects.create(name="Community Library")

# Add books to libraries
print("Adding books to libraries...")
library1.books.add(book1, book2, book5, book7)
library2.books.add(book3, book4, book6)
library3.books.add(book1, book3, book5, book8)

# Create librarians
print("Creating librarians...")
librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)
librarian3 = Librarian.objects.create(name="Carol Williams", library=library3)

print("\nDatabase populated successfully!")
print(f"Authors: {Author.objects.count()}")
print(f"Books: {Book.objects.count()}")
print(f"Libraries: {Library.objects.count()}")
print(f"Librarians: {Librarian.objects.count()}")
