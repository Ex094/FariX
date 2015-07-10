from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_id>\d+)/$', views.displayPost, name='displayPost'),
	url(r'^author/(?P<author>[a-zA-Z]+)/$', views.display_author_posts_list, name='display_author_posts_list'),
	url(r'^section/(?P<section>[a-zA-Z ]+)/$', views.display_section_post, name='display_section_post'),
	#url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	#url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	)