from django.db import models

# Author model represents a book writer.
# It has a name field to store the author's name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model represents a book written by an author.
# It includes title, publication year, and a foreign key to the Author.
# One author can have multiple books (One-to-Many Relationship).
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
