from __future__ import absolute_import, unicode_literals

from .celery import TaskQueue as celery_app

__all__ = ('celery_app')

default_app_config = 'api.apps.ApiConfig'