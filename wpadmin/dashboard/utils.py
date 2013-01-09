"""
Dashboard utilities.
"""

from wpadmin.utils import get_wpadmin_settings


def are_breadcrumbs_enabled(admin_site_name='admin'):
    """
    """
    if admin_site_name is None:
        admin_site_name = 'wpadmin_default'
    return get_wpadmin_settings(admin_site_name).get('dashboard', {}).get('breadcrumbs', True)
