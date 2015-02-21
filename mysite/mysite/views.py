from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

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
  

#hena ana ba3ml function esmaha hello, request must be
#the first parameter even law malhash lazma
#a view is just a function that takes a request as a
#parameter and returns an instance of response	

#ba3d ma bakteb el function lazem 23melaha activation
#fe el url.py file
