"""
Menu utilities.
"""
from fnmatch import fnmatch

from django.utils.importlib import import_module

from wpadmin.utils import get_wpadmin_settings, get_admin_site


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


# I had to copy (and slightly modify) those utils from django-admin-tools
# to override get_admin_site
def get_avail_models(context):
    """ Returns (model, perm,) for all models user can possibly see """
    items = []
    admin_site = get_admin_site(context)

    for model, model_admin in admin_site._registry.items():
        perms = model_admin.get_model_perms(context.get('request'))
        if True not in perms.values():
            continue
        items.append((model, perms,))
    return items


def filter_models(context, models, exclude):
    """
    Returns (model, perm,) for all models that match models/exclude patterns
    and are visible by current user.
    """
    items = get_avail_models(context)
    included = []
    full_name = lambda model: '%s.%s' % (model.__module__, model.__name__)

    # I believe that that implemented
    # O(len(patterns)*len(matched_patterns)*len(all_models))
    # algorithm is fine for model lists because they are small and admin
    # performance is not a bottleneck. If it is not the case then the code
    # should be optimized.

    if len(models) == 0:
        included = items
    else:
        for pattern in models:
            for item in items:
                model, perms = item
                if fnmatch(full_name(model), pattern) and item not in included:
                    included.append(item)

    result = included[:]
    for pattern in exclude:
        for item in included:
            model, perms = item
            if fnmatch(full_name(model), pattern):
                try:
                    result.remove(item)
                except ValueError:  # if the item was already removed skip
                    pass
    return result
