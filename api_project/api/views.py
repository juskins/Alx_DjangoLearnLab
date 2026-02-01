from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(generics.ListAPIView):
    """
    API view to retrieve list of all books.
    Uses BookSerializer to convert Book model instances to JSON.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling all CRUD operations on Book model.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
