import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

def setup_groups():
    # Get the content type for the Book model
    content_type = ContentType.objects.get_for_model(Book)

    # Define permissions
    permissions = {
        'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
        'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
        'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
        'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
    }

    # Create Groups and assign permissions
    
    # Viewers Group
    viewers_group, _ = Group.objects.get_or_create(name='Viewers')
    viewers_group.permissions.add(permissions['can_view'])

    # Editors Group
    editors_group, _ = Group.objects.get_or_create(name='Editors')
    editors_group.permissions.add(permissions['can_view'], permissions['can_create'], permissions['can_edit'])

    # Admins Group
    admins_group, _ = Group.objects.get_or_create(name='Admins')
    admins_group.permissions.add(*permissions.values())

    print("Groups and permissions setup complete.")

if __name__ == "__main__":
    setup_groups()
