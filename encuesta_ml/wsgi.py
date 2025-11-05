"""
WSGI config for encuesta_ml project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'encuesta_ml.settings')

application = get_wsgi_application()
