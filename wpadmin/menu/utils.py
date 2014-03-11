"""
Menu utilities.
"""
from fnmatch import fnmatch

from django.utils.importlib import import_module
from django.core.urlresolvers import reverse

from wpadmin.utils import (
    get_wpadmin_settings, get_admin_site, get_admin_site_name)


def get_menu_cls(menu, admin_site_name='admin'):
    """
    menu - menu name ('top' or 'left')
    """
    return get_wpadmin_settings(admin_site_name).get('menu', {}).get(menu, None)


def get_menu(menu, admin_site_name='admin'):
    """
    menu - menu name ('top' or 'left')
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

    for model, model_admin in list(admin_site._registry.items()):
        perms = model_admin.get_model_perms(context.get('request'))
        if True not in list(perms.values()):
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
    full_name = lambda m: '%s.%s' % (m.__module__, m.__name__)

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


class UserTestElementMixin(object):
    """
    Mixin which adds a method for checking if current user is allowed to see
    something (menu, menu item, etc.).
    """

    def is_user_allowed(self, user):
        """
        This method can be overwritten to check if current user can see this
        element.
        """
        return True


class AppListElementMixin(object):
    """
    Mixin class for AppList and ModelList MenuItem.
    """

    def _visible_models(self, context):

        included = self.models[:]
        excluded = self.exclude[:]

        if excluded and not included:
            included = ["*"]
        return filter_models(context, included, excluded)

    def _get_admin_app_list_url(self, model, context):
        """
        Returns the admin change url.
        """
        app_label = model._meta.app_label
        return reverse('%s:app_list' % get_admin_site_name(context),
                       args=(app_label,))

    def _get_admin_change_url(self, model, context):
        """
        Returns the admin change url.
        """
        app_label = model._meta.app_label
        return reverse('%s:%s_%s_changelist' % (get_admin_site_name(context),
                                                app_label,
                                                model.__name__.lower()))

    def _get_admin_add_url(self, model, context):
        """
        Returns the admin add url.
        """
        app_label = model._meta.app_label
        return reverse('%s:%s_%s_add' % (get_admin_site_name(context),
                                         app_label,
                                         model.__name__.lower()))

    def is_empty(self):
        return len(self.children) == 0

