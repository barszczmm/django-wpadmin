from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from .admin import admin, staff, user

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^adminpanel/', include(admin.urls)),
    url(r'^staffpanel/', include(staff.urls)),
    url(r'^userpanel/', include(user.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
