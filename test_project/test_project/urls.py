from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin as default_admin

from .admin import admin, staff, user

urlpatterns = patterns('',
    url(r'^admin/', include(default_admin.site.urls)),
    url(r'^adminpanel/', include(admin.urls)),
    url(r'^staffpanel/', include(staff.urls)),
    url(r'^userpanel/', include(user.urls)),
    #url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
