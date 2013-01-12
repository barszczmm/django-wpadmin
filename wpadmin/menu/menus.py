from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.core.urlresolvers import reverse
from django.conf import settings

from admin_tools.menu import Menu as ATMenu

from wpadmin.utils import UserTestElementMixin, get_admin_site_name
from wpadmin.menu import items


class Menu(ATMenu, UserTestElementMixin):
    """
    """

    icons = {}


class TopMenu(Menu):
    """
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
                url=reverse('%s:auth_user_change' % admin_site_name, args=(context['request'].user.id,)),
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
        if user.is_staff:
            return True
        return False

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

