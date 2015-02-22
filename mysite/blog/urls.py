from django.conf.urls import patterns, include, url
from blog.views import *

urlpatterns = patterns('blog.views',
	url(r'^$', 'index', name='home'),
	url(r'^view_post/(?P<post_id>\d+)$', 'view_post', name='view_post'),
)