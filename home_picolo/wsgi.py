"""
WSGI config for HinnAPI_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
path = '/var/www/home_picolo'

if path not in sys.path:
  sys.path.append(path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home_picolo.settings')

application = get_wsgi_application()

