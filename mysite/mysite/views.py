from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
import datetime 
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

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
def login_view(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		print username, password

		user = authenticate(username=username, password=password)
		print user
		if user is not None:
			if user.is_active:
				login(request, user)

				# Redirect to a success page.el url bta3 el homepage hena
				#return render_to_response('logout.html', {}, context_instance=RequestContext(request))
				return render_to_response('homepage.html', {}, context_instance=RequestContext(request))

			else:
				return HttpResponse('disabled account') # Return a 'disabled account' error message
		else:
			return HttpResponse('invalid login')# Return an 'invalid login' error message.
	else:
		return render_to_response('login.html', {}, context_instance=RequestContext(request))
def logout_view(request):
   	logout(request)
   	return render_to_response('login.html', {}, context_instance=RequestContext(request))
	
def invalid_login(request):
	#if request.POST:
		#return render_to_response('login.html', {}, context_instance=RequestContext(request))
		return render_to_response('invalid_login.html', {}, context_instance=RequestContext(request))
