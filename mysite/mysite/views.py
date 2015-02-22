from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
import datetime 
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("Hey Ana Fizo")

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def homepage(request):
	now = datetime.datetime.now()
	t = get_template('homepage.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html) 


def teampage(request):
	return render_to_response('team.html', {}, context_instance=RequestContext(request))
  

#hena ana ba3ml function esmaha hello, request must be
#the first parameter even law malhash lazma
#a view is just a function that takes a request as a
#parameter and returns an instance of response	

#ba3d ma bakteb el function lazem 23melaha activation
#fe el url.py file
