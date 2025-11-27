import os
from django.core.wsgi import get_wsgi_application

# Point to your project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'applaude_backend.settings')

# This is the entry point Gunicorn looks for
application = get_wsgi_application()
