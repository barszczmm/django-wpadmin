import urllib, hashlib
from django import template

from wpadmin.menu.utils import get_menu_cls, get_menu

register = template.Library()


class IsMenuEnabledNode(template.Node):

    def __init__(self, menu):
        """
        menu - menu name ('top' or 'left')
        """
        self.menu = menu

    def render(self, context):
        if get_menu_cls(self.menu, context.get('admin_site_name', None)) is None:
            enabled = False
        else:
            enabled = True
        context['wpadmin_is_%s_menu_enabled' % self.menu] = enabled
        return ''


def wpadmin_is_top_menu_enabled(parser, token):
    try:
        tag_name, admin_site_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument which is admin site name stored in template variable" % token.contents.split()[0])
    return IsMenuEnabledNode('top')

register.tag('wpadmin_is_top_menu_enabled', wpadmin_is_top_menu_enabled)


def wpadmin_is_left_menu_enabled(parser, token):
    try:
        tag_name, admin_site_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument which is admin site name stored in template variable" % token.contents.split()[0])
    return IsMenuEnabledNode('left')

register.tag('wpadmin_is_left_menu_enabled', wpadmin_is_left_menu_enabled)


def wpadmin_render_top_menu(context):
    admin_site_name = context.get('admin_site_name', None)
    menu = get_menu('top', admin_site_name)
    if menu:
        menu.init_with_context(context)
        context.update({
            'menu': menu,
        })
    return context

register.inclusion_tag('wpadmin/menu/top_menu.html', takes_context=True)(wpadmin_render_top_menu)


def wpadmin_render_left_menu(context):
    admin_site_name = context.get('admin_site_name', None)
    menu = get_menu('left', admin_site_name)
    if menu:
        menu.init_with_context(context)
        context.update({
            'menu': menu,
        })
    return context

register.inclusion_tag('wpadmin/menu/left_menu.html', takes_context=True)(wpadmin_render_left_menu)


def wpadmin_render_left_menu_top_most_item(context, item, icons):
    item.init_with_context(context)
    context.update({
        'item': item,
        'icons': icons,
    })
    return context

register.inclusion_tag('wpadmin/menu/left_menu_top_most_item.html', takes_context=True)(wpadmin_render_left_menu_top_most_item)


def wpadmin_render_left_menu_top_item(context, item, is_first, is_last, icons):
    item.init_with_context(context)
    if item.icon:
        icon = item.icon
    else:
        icon = icons.get(item.url, icons.get('wp-default-icon', 'icon-folder-open'))
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'icon': icon,
        'is_selected': item.is_selected(context['request']),
    })
    return context

register.inclusion_tag('wpadmin/menu/left_menu_top_item.html', takes_context=True)(wpadmin_render_left_menu_top_item)


def wpadmin_render_left_menu_item(context, item, is_first, is_last):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'is_selected': item.is_selected(context['request']),
    })
    return context

register.inclusion_tag('wpadmin/menu/left_menu_item.html', takes_context=True)(wpadmin_render_left_menu_item)


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
        'is_selected': item.is_selected(context['request']),
    })
    return context

register.inclusion_tag('wpadmin/menu/top_menu_top_item.html', takes_context=True)(wpadmin_render_top_menu_top_item)


def wpadmin_render_top_menu_item(context, item, is_first, is_last):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'is_selected': item.is_selected(context['request']),
    })
    return context

register.inclusion_tag('wpadmin/menu/top_menu_item.html', takes_context=True)(wpadmin_render_top_menu_item)


def wpadmin_render_bookmarks(context, item, is_first, is_last, is_selected):
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
        'is_selected': is_selected,
    })
    return context

register.inclusion_tag('wpadmin/menu/bookmarks.html', takes_context=True)(wpadmin_render_bookmarks)


def wpadmin_render_bookmark(context, item, is_first):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_selected': item.is_selected(context['request']),
    })
    return context

register.inclusion_tag('wpadmin/menu/bookmark.html', takes_context=True)(wpadmin_render_bookmark)


def wpadmin_render_user_tools(context, item, is_first, is_last):
    item.init_with_context(context)
    context.update({
        'item': item,
        'is_first': is_first,
        'is_last': is_last,
    })
    return context

register.inclusion_tag('wpadmin/menu/user_tools.html', takes_context=True)(wpadmin_render_user_tools)


def gravatar_url(user, size, https=True):
    default = 'wavatar'
    if https:
        gravatar_url = 'https'
    else:
        gravatar_url = 'http'
    gravatar_url += '://www.gravatar.com/avatar.php?'
    gravatar_url += urllib.urlencode({'gravatar_id':hashlib.md5(user.email.lower()).hexdigest(), 'default':default, 'size':str(size)})
    return gravatar_url

register.simple_tag(gravatar_url)


