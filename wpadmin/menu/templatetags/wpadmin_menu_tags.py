import urllib
import hashlib
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


def wpadmin_is_top_menu_enabled(parser, token):
    try:
        tag_name, admin_site_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument which is admin site name "
            + "stored in template variable" % token.contents.split()[0])
    return IsMenuEnabledNode('top')

register.tag('wpadmin_is_top_menu_enabled', wpadmin_is_top_menu_enabled)


def wpadmin_is_left_menu_enabled(parser, token):
    try:
        tag_name, admin_site_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument which is admin site name "
            + "stored in template variable" % token.contents.split()[0])
    return IsMenuEnabledNode('left')

register.tag('wpadmin_is_left_menu_enabled', wpadmin_is_left_menu_enabled)


def wpadmin_render_top_menu(context):
    menu = get_menu('top', get_admin_site_name(context))
    if menu:
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


def wpadmin_render_left_menu_top_most_item(context, item, icons):
    item.init_with_context(context)
    context.update({
        'item': item,
        'icons': icons,
        'is_user_allowed': item.is_user_allowed(context.get('request').user),
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/left_menu_top_most_item.html',
    takes_context=True)(wpadmin_render_left_menu_top_most_item)


def wpadmin_render_left_menu_top_item(context, item, is_first, is_last, icons):
    item.init_with_context(context)
    if item.icon:
        icon = item.icon
    else:
        icon = icons.get(item.url,
                         icons.get('wp-default-icon', 'icon-folder-open'))
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
    'wpadmin/menu/left_menu_top_item.html',
    takes_context=True)(wpadmin_render_left_menu_top_item)


def wpadmin_render_left_menu_item(context, item, is_first, is_last):
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
    'wpadmin/menu/left_menu_item.html',
    takes_context=True)(wpadmin_render_left_menu_item)


def wpadmin_render_top_menu_top_item(context, item, is_first, is_last, icons):
    item.init_with_context(context)
    if item.icon:
        icon = item.icon
    else:
        icon = icons.get(item.url, None)
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
    'wpadmin/menu/top_menu_top_item.html',
    takes_context=True)(wpadmin_render_top_menu_top_item)


def wpadmin_render_top_menu_item(context, item, is_first, is_last):
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
    'wpadmin/menu/top_menu_item.html',
    takes_context=True)(wpadmin_render_top_menu_item)


def wpadmin_render_bookmarks(context, item, is_first, is_last, is_selected,
                             is_user_allowed):
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'is_selected': is_selected,
        'is_user_allowed': is_user_allowed,
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/bookmarks.html',
    takes_context=True)(wpadmin_render_bookmarks)


def wpadmin_render_bookmark(context, item, is_first):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_selected': item.is_selected(context['request']),
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/bookmark.html',
    takes_context=True)(wpadmin_render_bookmark)


def wpadmin_render_user_tools(context, item, is_first, is_last):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'is_user_allowed': item.is_user_allowed(context.get('request').user),
    })
    return context

register.inclusion_tag(
    'wpadmin/menu/user_tools.html',
    takes_context=True)(wpadmin_render_user_tools)


def gravatar_url(user, size, https=True):
    default = 'wavatar'
    if https:
        gravatar_url = 'https'
    else:
        gravatar_url = 'http'
    gravatar_url += '://www.gravatar.com/avatar.php?'
    gravatar_url += urllib.urlencode({
        'gravatar_id': hashlib.md5(user.email.lower()).hexdigest(),
        'default': default,
        'size': str(size)})
    return gravatar_url

register.simple_tag(gravatar_url)

