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
    icons = {}

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])
        self.children = kwargs.get('children', [])

    def init_with_context(self, context):
        pass


class TopMenu(Menu):
    """
    Default top menu.
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
                site_name,
                url=site_url,
                css_classes=['branding', 'no-border'],
            ),
            items.MenuItem(
                capfirst(_('dashboard')),
                icon='icon-home',
                url=reverse('%s:index' % admin_site_name),
                description=capfirst(_('dashboard')),
            ),
            items.AppList(
                capfirst(_('applications')),
                icon='icon-tasks',
                exclude=('django.contrib.*',),
            ),
            items.AppList(
                capfirst(_('administration')),
                icon='icon-cogs',
                models=('django.contrib.*',),
            ),
            items.UserTools(
                css_classes=['float-right'],
                check_if_user_allowed=lambda user: user.is_staff,
            ),
            # items.Bookmarks(
            #    css_classes=['float-right', 'no-border'],
            #    check_if_user_allowed=lambda user: user.is_staff,
            # ),
        ]


class LeftMenu(Menu):
    """
    Default left menu.
    """

    icons = {
        'wp-default-icon': 'icon-folder-open',
        '/admin/auth/': 'icon-user',
        '/admin/sites/': 'icon-globe',
    }

    def is_user_allowed(self, user):
        """
        Only users that are staff are allowed to see this menu.
        """
        return user.is_staff

    def init_with_context(self, context):

        admin_site_name = get_admin_site_name(context)

        self.children += [
            items.MenuItem(
                title='',
                children=[
                    items.MenuItem(
                        capfirst(_('dashboard')),
                        icon='icon-home',
                        url=reverse('%s:index' % admin_site_name),
                        description=capfirst(_('dashboard')),
                    )
                ]
            ),
            items.AppList(
                capfirst(_('applications')),
                exclude=('django.contrib.*',),
            ),
            items.AppList(
                capfirst(_('administration')),
                models=('django.contrib.*',),
            ),
        ]

