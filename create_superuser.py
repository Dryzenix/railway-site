import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bezbreda.settings')
django.setup()

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'password123')
    print("Superuser created: admin / password123")
else:
    print("Superuser already exists")