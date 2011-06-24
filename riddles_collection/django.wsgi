import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'riddles_collection.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


PROJECT_DIR = os.path.dirname(__file__)
if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)
