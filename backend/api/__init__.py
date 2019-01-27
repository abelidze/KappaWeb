from __future__ import absolute_import, unicode_literals
from .celery import TaskQueue as celery_app
import os

__all__ = ('celery_app')

if os.environ.get('RUN_MAIN', None) != 'true':
    default_app_config = 'backend.api.apps.ApiConfig'
