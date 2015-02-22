from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, homepage, teampage
from mysite.settings import MEDIA_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', hello),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root' : MEDIA_ROOT}),
    url(r'^time$', current_datetime),
    url(r'^homepage$', homepage),
    url(r'^team$', teampage),

    
    
    
)

#first parameter howa el esm el bytktb fel link
#second parameter howa esm el view method

#for example when somebody visits the url /foo/, call
#the view function foo_view(), which is found in 
#views.py file

#the urlpatterns contains el urls
#y3ni lama aft7 1stp yeban 2ndp


