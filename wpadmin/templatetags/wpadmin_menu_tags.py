import hashlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from django import template

from wpadmin.utils import get_admin_site_name
from wpadmin.menu.utils import get_menu

register = template.Library()


class IsMenuEnabledNode(template.Node):

    def __init__(self, menu_name):
        """
        menu_name - menu name ('top' or 'left')
        """
        self.menu_name = menu_name

    def render(self, context):
        menu = get_menu(self.menu_name, get_admin_site_name(context))
        if menu and menu.is_user_allowed(context.get('request').user):
            enabled = True
        else:
            enabled = False
        context['wpadmin_is_%s_menu_enabled' % self.menu_name] = enabled
        return ''


def wpadmin_is_left_menu_enabled(parser, token):
    return IsMenuEnabledNode('left')

register.tag('wpadmin_is_left_menu_enabled', wpadmin_is_left_menu_enabled)


def wpadmin_render_top_menu(context):
    menu = get_menu('top', get_admin_site_name(context))
    if not menu:
        from wpadmin.menu.menus import DefaultTopMenu
        menu = DefaultTopMenu()
    menu.init_with_context(context)
    context.update({
        'menu': menu,
        'is_user_allowed': menu.is_user_allowed(context.get('request').user),
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/top_menu.html',
    takes_context=True)(wpadmin_render_top_menu)


def wpadmin_render_left_menu(context):
    menu = get_menu('left', get_admin_site_name(context))
    if menu:
        menu.init_with_context(context)
        context.update({
            'menu': menu,
            'is_user_allowed': menu.is_user_allowed(context.get('request').user),
        })
    return context

register.inclusion_tag(
    'wpadmin/menu/left_menu.html',
    takes_context=True)(wpadmin_render_left_menu)


def wpadmin_render_menu_top_item(context, item, is_first, is_last):
    item.init_with_context(context)
    if item.icon:
        icon = item.icon
    else:
        icon = 'fa-folder-o'
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'icon': icon,
        'is_selected': item.is_selected(context.get('request')),
        'is_user_allowed': item.is_user_allowed(context.get('request').user),
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/menu_top_item.html',
    takes_context=True)(wpadmin_render_menu_top_item)


def wpadmin_render_menu_item(context, item, is_first, is_last):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'is_selected': item.is_selected(context.get('request')),
        'is_user_allowed': item.is_user_allowed(context.get('request').user),
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/menu_item.html',
    takes_context=True)(wpadmin_render_menu_item)


def wpadmin_render_user_tools(context, item, is_first, is_last):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'is_user_allowed': context.get('request').user.is_authenticated()
        and item.is_user_allowed(context.get('request').user),
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/user_tools.html',
    takes_context=True)(wpadmin_render_user_tools)


def gravatar_url(user, size, https=True):
    default = 'retro'
    if https:
        url = 'https'
    else:
        url = 'http'
    url += '://www.gravatar.com/avatar.php?'
    if hasattr(user, 'email') and user.email:
        gravatar_id = hashlib.md5(user.email.lower().encode('utf-8')).hexdigest()
    else:
        gravatar_id = '00000000000000000000000000000000'
    url += urlencode({
        'gravatar_id': gravatar_id,
        'default': default,
        'size': str(size)})
    return url

register.simple_tag(gravatar_url)

