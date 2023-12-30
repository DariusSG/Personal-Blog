"""
ASGI config for ProjectWeb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectWeb.settings')
os.environ.setdefault('DEBUG', 'True')

application = get_asgi_application()
