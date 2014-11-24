from django import template
from django.utils.translation import ugettext_lazy as _

from wpadmin.utils import (
    get_admin_site_name, get_wpadmin_settings, are_breadcrumbs_enabled)

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


class AreBreadcrumbsEnabledNode(template.Node):

    def render(self, context):
        context['wpadmin_are_breadcrumbs_enabled'] = are_breadcrumbs_enabled(
            get_admin_site_name(context))
        return ''


def wpadmin_are_breadcrumbs_enabled(parser, token):
    return AreBreadcrumbsEnabledNode()

register.tag('wpadmin_are_breadcrumbs_enabled', wpadmin_are_breadcrumbs_enabled)


def wpadmin_render_custom_title(context):
    # Translators: This is already translated in Django
    return get_wpadmin_settings(get_admin_site_name(context)) \
        .get('title', context.get('site_title', _('Django site admin')))

register.simple_tag(takes_context=True)(wpadmin_render_custom_title)

