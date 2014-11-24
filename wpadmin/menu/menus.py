from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site, get_admin_site_name
from wpadmin.menu.utils import UserTestElementMixin
from wpadmin.menu import items


class Menu(UserTestElementMixin):
    """
    Base menu.
    """
    children = None

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])
        self.children = kwargs.get('children', [])

    def init_with_context(self, context):
        pass


class DefaultTopMenu(Menu):
    """
    Default top menu which mimics default Django admin header.
    This one is used if there is no top menu specified in Django WP Admin settings.
    """

    def init_with_context(self, context):

        self.children += [
            items.MenuItem(
                title=get_admin_site(context).site_header,
                url=None,
                icon='fa-gears',
                css_styles='font-size: 1.5em;',
            ),
            items.UserTools(
                css_styles='float: right;',
                is_user_allowed=lambda user: user.is_active and user.is_staff,
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
            site_name = _('Site')
            site_url = '/'

        self.children += [
            items.MenuItem(
                title=site_name,
                url=site_url,
                icon='fa-bullseye',
                css_styles='font-size: 1.5em;',
            ),
            items.MenuItem(
                title=_('Dashboard'),
                icon='fa-tachometer',
                url=reverse('%s:index' % admin_site_name),
                description=_('Dashboard'),
            ),
            items.UserTools(
                css_styles='float: right;',
                is_user_allowed=lambda user: user.is_staff,
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
                    title=_('Dashboard'),
                    icon='fa-tachometer',
                    url=reverse('%s:index' % admin_site_name),
                    description=_('Dashboard'),
                ),
                items.AppList(
                    title=_('Applications'),
                    description=_('Applications'),
                    exclude=('django.contrib.*',),
                    icon='fa-tasks',
                ),
                items.AppList(
                    title=_('Administration'),
                    description=_('Administration'),
                    models=('django.contrib.*',),
                    icon='fa-cog',
                ),
            ]

