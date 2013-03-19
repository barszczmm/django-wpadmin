from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site_name
from wpadmin.menu import items
from wpadmin.menu.menus import Menu


class AdminTopMenu(Menu):

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
                check_if_user_allowed=lambda user: user.is_superuser,
            ),
            items.AppList(
                capfirst(_('administration')),
                icon='icon-cogs',
                models=('django.contrib.*',),
                check_if_user_allowed=lambda user: user.is_superuser,
            ),
            items.UserTools(
                url=reverse('%s:auth_user_change' % admin_site_name,
                            args=(context['request'].user.id,)),
                css_classes=['float-right'],
                check_if_user_allowed=lambda user: user.is_superuser,
            ),
        ]


class StaffTopMenu(Menu):

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
                check_if_user_allowed=lambda user: user.is_staff,
            ),
            items.AppList(
                capfirst(_('administration')),
                icon='icon-cogs',
                models=('django.contrib.*',),
                check_if_user_allowed=lambda user: user.is_staff,
            ),
            items.UserTools(
                url=None,
                css_classes=['float-right'],
                check_if_user_allowed=lambda user: user.is_staff,
            ),
        ]


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
                check_if_user_allowed=lambda user: user.groups.filter(
                    name='users').count(),
            ),
            items.AppList(
                capfirst(_('administration')),
                icon='icon-cogs',
                models=('django.contrib.*',),
                check_if_user_allowed=lambda user: user.groups.filter(
                    name='users').count(),
            ),
            items.UserTools(
                url=None,
                css_classes=['float-right'],
                check_if_user_allowed=lambda user: user.groups.filter(
                    name='users').count(),
            ),
        ]


class AdminLeftMenu(Menu):

    icons = {
        'wp-default-icon': 'icon-folder-open',
        '/admin/auth/user/': 'icon-user',
        '/admin/auth/group/': 'icon-group',
        '/admin/sites/site/': 'icon-globe',
    }

    def is_user_allowed(self, user):
        """
        Only users that are superusers are allowed to see this menu.
        """
        return user.is_superuser

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
            items.MenuItem(
                capfirst(_('catalogue')),
                children=[
                    items.ModelList(
                        capfirst(_('items')),
                        icon='icon-book',
                        models=(
                            'books.models.Book',
                            'cds.models.Cd',
                            'dvds.models.Dvd',
                        ),
                    ),
                    items.ModelList(
                        capfirst(_('categories')),
                        models=(
                            'books.models.BookCategory',
                            'cds.models.CdCategory',
                            'dvds.models.DvdCategory',
                        ),
                    ),
                    items.ModelList(
                        capfirst(_('authors')),
                        icon='icon-quote-right',
                        models=('authors.models.Author',),
                    ),
                ],
            ),
            items.ModelList(
                capfirst(_('users')),
                models=('django.contrib.auth.*',),
            ),
            items.ModelList(
                capfirst(_('administration')),
                models=('django.contrib.sites.*',),
            ),
        ]


class StaffLeftMenu(Menu):

    icons = {
        'wp-default-icon': 'icon-folder-open',
        '/staff/authors/author/': 'icon-quote-right',
        '/staff/books/bookcategory/': 'icon-book',
        '/staff/cds/cdcategory/': 'icon-music',
        '/staff/dvds/dvdcategory/': 'icon-film',
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
            items.ModelList(
                capfirst(_('catalogue')),
                models=(
                    'authors.models.Author',
                    'books.models.BookCategory',
                    'cds.models.CdCategory',
                    'dvds.models.DvdCategory',
                ),
            ),
        ]


class UserLeftMenu(Menu):

    icons = {
        'wp-default-icon': 'icon-folder-open',
        '/user/books/book/': 'icon-book',
        '/user/cds/cd/': 'icon-music',
        '/user/dvds/dvd/': 'icon-film',
    }

    def is_user_allowed(self, user):
        """
        Only users that are in 'users' group are allowed to see this menu.
        """
        return user.groups.filter(name='users').count()

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
            items.ModelList(
                capfirst(_('my...')),
                models=(
                    'books.models.Book',
                    'cds.models.Cd',
                    'dvds.models.Dvd',
                ),
            ),
        ]

