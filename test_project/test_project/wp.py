from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site_name
from wpadmin.menu import items
from wpadmin.menu.menus import Menu


class UserTopMenu(Menu):

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
                capfirst(_('dashboard')),
                icon='fa-tachometer',
                url=reverse('%s:index' % admin_site_name),
                description=capfirst(_('dashboard')),
            ),
            items.AppList(
                capfirst(_('applications')),
                icon='fa-tasks',
                exclude=('django.contrib.*',),
                check_if_user_allowed=lambda user: user.groups.filter(
                    name='users').count(),
            ),
            items.AppList(
                capfirst(_('administration')),
                icon='fa-cog',
                models=('django.contrib.*',),
                check_if_user_allowed=lambda user: user.groups.filter(
                    name='users').count(),
            ),
            items.UserTools(
                css_styles='float: right;',
                check_if_user_allowed=lambda user: user.groups.filter(
                    name='users').count(),
            ),
        ]


class UserLeftMenu(Menu):

    def is_user_allowed(self, user):
        """
        Only users that are in 'users' group are allowed to see this menu.
        """
        return user.groups.filter(name='users').count()

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
                items.MenuItem(
                    title=_('Books'),
                    icon='fa-book',
                    url=reverse('%s:books_book_changelist' % admin_site_name),
                ),
                items.MenuItem(
                    title=_('CDs'),
                    icon='fa-music',
                    url=reverse('%s:cds_cd_changelist' % admin_site_name),
                ),
                items.MenuItem(
                    title=_('DVDs'),
                    icon='fa-film',
                    url=reverse('%s:dvds_dvd_changelist' % admin_site_name),
                ),
            ]

