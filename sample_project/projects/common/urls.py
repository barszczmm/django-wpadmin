try:
    from django.conf.urls import patterns, include, url
except ImportError:
    from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from admin import admin, staff, user

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django14.views.home', name='home'),
    # url(r'^django14/', include('django14.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^admin/', include(admin.urls)),
    url(r'^staff/', include(staff.urls)),
    url(r'^user/', include(user.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
