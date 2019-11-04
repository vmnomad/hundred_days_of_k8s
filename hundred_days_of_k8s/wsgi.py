"""
WSGI config for hundred_days_of_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hundred_days_of_k8s.settings')

from dj_static import Cling
application = Cling(get_wsgi_application())
