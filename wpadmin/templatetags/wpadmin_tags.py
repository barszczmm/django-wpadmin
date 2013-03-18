from django import template

from wpadmin.utils import get_admin_site_name, get_wpadmin_settings

register = template.Library()


def wpadmin_render_custom_style(context):
    custom_style_path = get_wpadmin_settings(get_admin_site_name(context)) \
        .get('custom_style', None)
    if custom_style_path:
        return '<link type="text/css" rel="stylesheet" href="%s" />' \
            % custom_style_path
    else:
        return ''

register.simple_tag(takes_context=True)(wpadmin_render_custom_style)