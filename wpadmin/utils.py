"""
WPadmin utilities.
"""

from django.conf import settings
from django.utils.importlib import import_module
from django.contrib import admin


def get_wpadmin_settings(admin_site_name='admin'):
    """
    Get WPadmin settings for specified admin site.
    """
    return getattr(settings, 'WPADMIN', {}).get(admin_site_name, {})


def get_admin_site_name(context):
    """
    Get admin site name from context.
    First it tries to find variable named admin_site_name in context.
    If this variable is not available, admin site name is taken from request path
    (it is first part of path - between first and second slash).
    """
    admin_site_name = context.get('admin_site_name', None)
    if admin_site_name is None:
        admin_site_name = context.get('request').path.split('/')[1]
    return admin_site_name


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
