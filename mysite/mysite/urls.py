from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    
    #For Blog
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^blog/', 'blog.views.index', name="blog_index"), #For main page link
    url(r'^login/$', 'blog.views.login_user'),
    url(r'^logout/$', 'blog.views.user_logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
