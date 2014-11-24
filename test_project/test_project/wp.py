from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site_name
from wpadmin.menu import items
from wpadmin.menu.menus import Menu


class UserTopMenu(Menu):

    def my_user_check(self, user):
        """
        Custom helper method for hiding some menu items from not allowed users.
        """
        return user.groups.filter(name='users').exists()

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
        ]

        if self.my_user_check(context.get('request').user):
            self.children += [
                items.AppList(
                    title=_('Applications'),
                    icon='fa-tasks',
                    exclude=('django.contrib.*',),
                ),
                items.AppList(
                    title=_('Administration'),
                    icon='fa-cog',
                    models=('django.contrib.*',),
                ),
                items.UserTools(
                    css_styles='float: right;',
                ),
            ]

        self.children += [
            items.MenuItem(
                title=_('Color theme'),
                icon='fa-paint-brush',
                description=_('Change color theme'),
                css_styles='float: right;',
                children=[
                    items.MenuItem(
                        title='Blue',
                        url='javascript:change_color_theme("blue");',
                    ),
                    items.MenuItem(
                        title='Coffee',
                        url='javascript:change_color_theme("coffee");',
                    ),
                    items.MenuItem(
                        title='Default',
                        url='javascript:change_color_theme("default");',
                    ),
                    items.MenuItem(
                        title='Ectoplasm',
                        url='javascript:change_color_theme("ectoplasm");',
                    ),
                    items.MenuItem(
                        title='Light',
                        url='javascript:change_color_theme("light");',
                    ),
                    items.MenuItem(
                        title='Milo',
                        url='javascript:change_color_theme("milo");',
                    ),
                    items.MenuItem(
                        title='Milo Light',
                        url='javascript:change_color_theme("milo-light");',
                    ),
                    items.MenuItem(
                        title='Midnight',
                        url='javascript:change_color_theme("midnight");',
                    ),
                    items.MenuItem(
                        title='Ocean',
                        url='javascript:change_color_theme("ocean");',
                    ),
                    items.MenuItem(
                        title='Sunrise',
                        url='javascript:change_color_theme("sunrise");',
                    ),
                ]
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
                    title=_('Dashboard'),
                    icon='fa-tachometer',
                    url=reverse('%s:index' % admin_site_name),
                    description=_('Dashboard'),
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

