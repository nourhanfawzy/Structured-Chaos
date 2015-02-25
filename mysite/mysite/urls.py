from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from mysite.views import hello, current_datetime, homepage, teampage, signup, welcome, homepagesignup, welcomesignup
=======
from mysite.views import hello, current_datetime, homepage, teampage, signup
>>>>>>> 631e6fd596733e56156dae6ec73f9c975251b479
from mysite.settings import MEDIA_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/viewallposts.html','blog.views.viewallposts'),
    url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', hello),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root' : MEDIA_ROOT}),
    url(r'^time$', current_datetime),
    url(r'^homepage$', homepage),
<<<<<<< HEAD

    url(r'^team.html$', 'mysite.views.teampage'),

    url(r'^signup.html$', signup),

=======
    url(r'^team.html$', 'mysite.views.teampage'),
	url(r'^signup$', signup),
>>>>>>> 631e6fd596733e56156dae6ec73f9c975251b479
    url(r'^team$', teampage),
	url(r'^login$', 'mysite.views.login_view'),
	url(r'^logout$', 'mysite.views.logout_view'),
	url(r'^invalid$', 'mysite.views.invalid_login'),
	url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD

    
=======
>>>>>>> 631e6fd596733e56156dae6ec73f9c975251b479
    url(r'^login$', 'mysite.views.login_view'),
	url(r'^logout$', 'mysite.views.logout_view'),
	url(r'^invalid$', 'mysite.views.invalid_login'),
	url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^welcome$', welcome),
    url(r'^welcomesignup$', welcomesignup),
    url(r'^homepagesignup$', homepagesignup),
=======
>>>>>>> 631e6fd596733e56156dae6ec73f9c975251b479

    url(r'^mahira.html$', 'mysite.views.mahira'),
    url(r'^fizo.html$', 'mysite.views.fizo'),
    url(r'^youssef.html$', 'mysite.views.youssef'),
    url(r'^omar.html$', 'mysite.views.omar'),
    url(r'^nourhans.html$', 'mysite.views.nourhans'),
    url(r'^nadaemad.html$', 'mysite.views.nadaemad'),
    url(r'^nadayasser.html$', 'mysite.views.nadayasser'),
    
)

#first parameter howa el esm el bytktb fel link
#second parameter howa esm el view method

#for example when somebody visits the url /foo/, call
#the view function foo_view(), which is found in 
#views.py file

#the urlpatterns contains el urls
#y3ni lama aft7 1stp yeban 2ndp


