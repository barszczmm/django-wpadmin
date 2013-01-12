"""
Dashboard utilities.
"""

from wpadmin.utils import get_wpadmin_settings


def are_breadcrumbs_enabled(admin_site_name='admin'):
    """
    """
    return get_wpadmin_settings(admin_site_name).get('dashboard', {}).get('breadcrumbs', True)
