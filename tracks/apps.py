from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TracksConfig(AppConfig):
    name = 'tracks'
    label = 'tracks'
    verbose_name = _('Tracks')
    default_auto_field = 'django.db.models.BigAutoField'
