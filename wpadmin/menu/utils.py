"""
Menu utilities.
"""

from django.utils.importlib import import_module

from wpadmin.utils import get_wpadmin_settings


def get_menu_cls(menu, admin_site_name='admin'):
    """
    """
    return get_wpadmin_settings(admin_site_name).get('menu', {}).get(menu, None)


def get_menu(menu, admin_site_name='admin'):
    """
    """
    menu_cls = get_menu_cls(menu, admin_site_name)
    if menu_cls:
        mod, inst = menu_cls.rsplit('.', 1)
        mod = import_module(mod)
        return getattr(mod, inst)()
    return None

