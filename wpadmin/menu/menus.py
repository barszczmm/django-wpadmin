from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site_name
from wpadmin.menu.utils import UserTestElementMixin
from wpadmin.menu import items


class Menu(UserTestElementMixin):
    """
    Base menu.
    """
    template = 'wpadmin/menu/menu.html'
    children = None

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])
        self.children = kwargs.get('children', [])

    def is_user_allowed(self, user):
        """
        Check if specified user is allowed to see this menu.
        """
        return True

    def init_with_context(self, context):
        pass


class DefaultTopMenu(Menu):
    """
    Default top menu which mimics default Django admin header.
    """

    def init_with_context(self, context):

        self.children += [
            items.MenuItem(
                title=_('Django administration'),
                url=None,
                icon='fa-gears',
                css_styles='font-size: 1.5em;',
            ),
            items.UserTools(
                css_styles='float: right;',
                check_if_user_allowed=lambda user: user.is_active and user.is_staff,
            ),
        ]


class BasicTopMenu(Menu):
    """
    Basic default top menu.
    """

    def init_with_context(self, context):

        admin_site_name = get_admin_site_name(context)

        if 'django.contrib.sites' in settings.INSTALLED_APPS:
            from django.contrib.sites.models import Site
            site_name = Site.objects.get_current().name
            site_url = 'http://' + Site.objects.get_current().domain
        else:
            site_name = capfirst(_('site'))
            site_url = '/'

        self.children += [
            items.MenuItem(
                title=site_name,
                url=site_url,
                icon='fa-bullseye',
                css_styles='font-size: 1.5em;',
            ),
            items.MenuItem(
                title=capfirst(_('dashboard')),
                icon='fa-tachometer',
                url=reverse('%s:index' % admin_site_name),
                description=capfirst(_('dashboard')),
            ),
            items.UserTools(
                css_styles='float: right;',
                check_if_user_allowed=lambda user: user.is_staff,
            ),
        ]


class BasicLeftMenu(Menu):
    """
    Basic default left menu.
    """

    def is_user_allowed(self, user):
        """
        Only users that are staff are allowed to see this menu.
        """
        return user.is_staff

    def init_with_context(self, context):

        if self.is_user_allowed(context.get('request').user):

            admin_site_name = get_admin_site_name(context)

            self.children += [
                items.MenuItem(
                    title=capfirst(_('dashboard')),
                    icon='fa-tachometer',
                    url=reverse('%s:index' % admin_site_name),
                    description=capfirst(_('dashboard')),
                ),
                items.AppList(
                    title=capfirst(_('applications')),
                    description=capfirst(_('applications')),
                    exclude=('django.contrib.*',),
                    icon='fa-tasks',
                ),
                items.AppList(
                    title=capfirst(_('administration')),
                    description=capfirst(_('administration')),
                    models=('django.contrib.*',),
                    icon='fa-cog',
                ),
            ]

