from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
import datetime 
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect

from django.core.context_processors import csrf
#from django.contrub.auth.forms import UserCreationForm
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


<<<<<<< HEAD

=======
#ba3d ma bakteb el function lazem 23melaha activation
#fe el url.py file
>>>>>>> 9e8e84b410efcb73397a0f662bf04ad5faacb17a
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
<<<<<<< HEAD
				return render_to_response('welcomesignup.html', {'user':user}, context_instance=RequestContext(request))
=======
				return render_to_response('homepage.html', {}, context_instance=RequestContext(request))
>>>>>>> 9e8e84b410efcb73397a0f662bf04ad5faacb17a

			else:
				return HttpResponse('disabled account') # Return a 'disabled account' error message
		else:
<<<<<<< HEAD
			return render_to_response('invalid_login.html')# Return an 'invalid login' error message.
	else:
		return render_to_response('login.html', {}, context_instance=RequestContext(request))

def signup(request):
	if request.POST:
		name = request.POST['name']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		sex = request.POST['sex']
		User(name=name, email=email, username=username, password=password, cpassword=cpassword, sex=sex).save()
	
	return render_to_response('signup.html', {}, context_instance=RequestContext(request))	
	

=======
			return HttpResponse('invalid login')# Return an 'invalid login' error message.
	else:
		return render_to_response('login.html', {}, context_instance=RequestContext(request))
>>>>>>> 9e8e84b410efcb73397a0f662bf04ad5faacb17a
def logout_view(request):
   	logout(request)
   	return render_to_response('login.html', {}, context_instance=RequestContext(request))
	
def invalid_login(request):
	#if request.POST:
		#return render_to_response('login.html', {}, context_instance=RequestContext(request))
		return render_to_response('invalid_login.html', {}, context_instance=RequestContext(request))
<<<<<<< HEAD
	#else:
		#pass



def mahira(request):
	return render_to_response('mahira.html', {}, context_instance=RequestContext(request))

def omar(request):
	return render_to_response('omar.html', {}, context_instance=RequestContext(request))

def nourhans(request):
	return render_to_response('nourhans.html', {}, context_instance=RequestContext(request))

def youssef(request):
	return render_to_response('youssef.html', {}, context_instance=RequestContext(request))

def nadaemad(request):
	return render_to_response('nadaemad.html', {}, context_instance=RequestContext(request))

def nadayasser(request):
	return render_to_response('nadayasser.html', {}, context_instance=RequestContext(request))

def fizo(request):
	return render_to_response('fizo.html', {}, context_instance=RequestContext(request))


def welcome(request):
	return render_to_response('welcome.html', {}, context_instance=RequestContext(request))

def welcomesignup(request):
	return render_to_response('welcomesignup.html', {}, context_instance=RequestContext(request))


def homepagesignup(request):
	return render_to_response('homepagesignup.html', {}, context_instance=RequestContext(request))








=======
>>>>>>> 9e8e84b410efcb73397a0f662bf04ad5faacb17a
