from django import template

from wpadmin.dashboard.utils import are_breadcrumbs_enabled

register = template.Library()


class AreBreadcrumbsEnabledNode(template.Node):

    def render(self, context):
        context['wpadmin_are_breadcrumbs_enabled'] = are_breadcrumbs_enabled(context.get('admin_site_name', None))
        return ''

def wpadmin_are_breadcrumbs_enabled(parser, token):
    try:
        tag_name, admin_site_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument which is admin site name stored in template variable" % token.contents.split()[0])
    return AreBreadcrumbsEnabledNode()

register.tag('wpadmin_are_breadcrumbs_enabled', wpadmin_are_breadcrumbs_enabled)
