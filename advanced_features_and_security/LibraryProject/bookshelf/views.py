from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

from django.db.models import Q

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    query = request.GET.get('q')
    if query:
        # Using Django ORM filter() which handles parameterization safely to prevent SQL injection
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

from .forms import ExampleForm

def form_example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process validated data safely
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Simplified for the task, usually contains a form
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
