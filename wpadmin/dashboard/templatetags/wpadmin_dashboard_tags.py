from django import template
from django.utils.translation import ugettext_lazy as _

from wpadmin.utils import get_admin_site_name, get_wpadmin_settings
from wpadmin.dashboard.utils import are_breadcrumbs_enabled

register = template.Library()


class AreBreadcrumbsEnabledNode(template.Node):

    def render(self, context):
        context['wpadmin_are_breadcrumbs_enabled'] = are_breadcrumbs_enabled(
            get_admin_site_name(context))
        return ''


def wpadmin_are_breadcrumbs_enabled(parser, token):
    try:
        tag_name, admin_site_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument which is admin site name "
            + "stored in template variable" % token.contents.split()[0])
    return AreBreadcrumbsEnabledNode()

register.tag('wpadmin_are_breadcrumbs_enabled', wpadmin_are_breadcrumbs_enabled)


def wpadmin_render_custom_title(context):
    return get_wpadmin_settings(get_admin_site_name(context)) \
        .get('title', _('Django site admin'))

register.simple_tag(takes_context=True)(wpadmin_render_custom_title)
