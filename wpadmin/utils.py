"""
WPadmin utilities.
"""

from django.conf import settings


def get_wpadmin_settings(admin_site_name='admin'):
    """
    """
    return getattr(settings, 'WPADMIN', {}).get(admin_site_name, {})
