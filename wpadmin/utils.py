"""
WPadmin utilities.
"""

from django.conf import settings


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


def get_wpadmin_settings(admin_site_name='admin'):
    """
    Gets WPadmin settings for specified admin site.
    """
    return getattr(settings, 'WPADMIN', {}).get(admin_site_name, {})


class UserTestElementMixin(object):
    """
    Mixin which adds a method for checking is current user is allowed to see
    something (menu, menu item, etc.).
    """

    # this may be set to some callable when class is instantiated
    check_if_user_allowed = None

    def is_user_allowed(self, user):
        """
        This method can be overwritten to check if current user can see this
        element.
        """
        if callable(self.check_if_user_allowed):
            return self.check_if_user_allowed(user)
        return True
