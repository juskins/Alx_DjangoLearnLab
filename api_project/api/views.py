from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(generics.ListAPIView):
    """
    API view to retrieve list of all books.
    Uses BookSerializer to convert Book model instances to JSON.
    Requires authentication to access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling all CRUD operations on Book model.
    Provides list, create, retrieve, update, and destroy actions.
    
    Permissions:
    - List and Retrieve: Available to authenticated users
    - Create, Update, Delete: Available to authenticated users
    
    Authentication:
    - Token Authentication: Include 'Authorization: Token <your-token>' in request headers
    - Session Authentication: Browser-based authentication for browsable API
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for all operations
