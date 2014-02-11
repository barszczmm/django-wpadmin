"""
WPadmin utilities.
"""

from django.conf import settings
from django.utils.importlib import import_module
from django.contrib import admin
from django.utils.translation import get_language_from_path


def get_wpadmin_settings(admin_site_name='admin'):
    """
    Get WPadmin settings for specified admin site.
    """
    return getattr(settings, 'WPADMIN', {}).get(admin_site_name, {})


def get_admin_site_name(context):
    """
    Get admin site name from request from context.
    Admin site name is taken from request path:
    * it is first part of path - between first and second slash if there is no
    lang prefix
    * or second part fo path - between second and third slash
    """
    path = context.get('request').path
    lang = get_language_from_path(path)
    path = path.split('/')
    if lang and path[1] == lang:
        return path[2]
    return path[1]


def get_admin_site(context):
    """
    Get admin site instance.
    """
    admin_site = get_wpadmin_settings(get_admin_site_name(context)) \
        .get('admin_site')
    if admin_site:
        mod, inst = admin_site.rsplit('.', 1)
        mod = import_module(mod)
        return getattr(mod, inst)
    else:
        return admin.site


def are_breadcrumbs_enabled(admin_site_name='admin'):
    """
    """
    return get_wpadmin_settings(admin_site_name).get('dashboard', {}) \
        .get('breadcrumbs', True)

