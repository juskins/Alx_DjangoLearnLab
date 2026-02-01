from django.db import models

# Create your models here.

class Book(models.Model):
    """
    Book model representing a book with title and author.
    This simple model is designed for API development.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
