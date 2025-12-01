import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_system.settings')
django.setup()

from core.models import User

try:
    user = User.objects.get(username='admin')
    user.set_password('admin123')
    user.save()
    print('✓ Password set successfully!')
    print('Username: admin')
    print('Password: admin123')
except User.DoesNotExist:
    print('✗ Admin user not found')
