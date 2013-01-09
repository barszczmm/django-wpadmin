from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from admin_tools.utils import AppListElementMixin
from admin_tools.menu.items import MenuItem as ATMenuItem, \
                                   AppList as ATAppList, \
                                   ModelList as ATModelList



class MenuItem(ATMenuItem):

    url = None
    add_url = None
    icon = None

    def is_selected(self, request):
        current_url = request.path
        return self.url == current_url or \
            self.add_url == current_url or \
            len([c for c in self.children if c.is_selected(request)]) > 0


class AppList(ATAppList):

    url = None
    add_url = None
    icon = None

    def init_with_context(self, context):
        """
        Please refer to the :meth:`~admin_tools.menu.items.MenuItem.init_with_context`
        documentation from :class:`~admin_tools.menu.items.MenuItem` class.
        """
        items = self._visible_models(context['request'])
        apps = {}
        for model, perms in items:
            if not perms['change']:
                continue
            app_label = model._meta.app_label
            if app_label not in apps:
                apps[app_label] = {
                    'title': capfirst(_(app_label.title())),
                    'url': self._get_admin_app_list_url(model, context),
                    'models': []
                }
            apps[app_label]['models'].append({
                'title': capfirst(model._meta.verbose_name_plural),
                'url': self._get_admin_change_url(model, context),
                'add_url': self._get_admin_add_url(model, context),
                'description': _(u"Change"),
            })

        apps_sorted = apps.keys()
        apps_sorted.sort()
        for app in apps_sorted:
            app_dict = apps[app]
            item = MenuItem(title=app_dict['title'], url=app_dict['url'], description=app_dict['title'])
            # sort model list alphabetically
            apps[app]['models'].sort(lambda x, y: cmp(x['title'], y['title']))
            for model_dict in apps[app]['models']:
                model_item = MenuItem(**model_dict)
                model_item.add_url = model_dict['add_url']
                item.children.append(model_item)
            self.children.append(item)


class ModelList(ATModelList):

    url = None
    add_url = None
    icon = None

    def init_with_context(self, context):
        """
        Please refer to the :meth:`~admin_tools.menu.items.MenuItem.init_with_context`
        documentation from :class:`~admin_tools.menu.items.MenuItem` class.
        """
        items = self._visible_models(context['request'])
        for model, perms in items:
            if not perms['change']:
                continue
            title = capfirst(model._meta.verbose_name_plural)
            url = self._get_admin_change_url(model, context)
            add_url = self._get_admin_add_url(model, context)
            item = MenuItem(title=title, url=url, description=title)
            item.add_url = add_url
            self.children.append(item)


class UserTools(MenuItem):

    is_user_tools = True
    css_classes = ['float-right']


# class Bookmarks(MenuItem, AppListElementMixin):
#
#    title = _('Bookmarks')
#    icon = 'icon-bookmark'
#    css_classes = ['float-right', 'bookmarks']
#    is_bookmarks = True
#
#    def init_with_context(self, context):
#
#        from admin_tools.menu.models import Bookmark
#
#        for b in Bookmark.objects.filter(user=context['request'].user):
#            self.children.append(MenuItem(mark_safe(b.title), b.url, is_bookmark=True))


