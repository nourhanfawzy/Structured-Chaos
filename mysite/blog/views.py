from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import post
from django.template import Context, loader
from django.http import HttpResponse
import datetime

from django.core.mail import send_mail
from django.core.files import File
import os


from django.contrib.auth.models import User
from mysite.settings import  DEBUG

from blog.models import Postt, Commentt
import random, datetime
from itertools import chain


def home(request):
    # entries = posts.objects.all()
    entries = post.objects.all()
    now = datetime.datetime.now()
    t = get_template('index.html')
    # html = t.render({'posts':entries})
    return render_to_response('index.html',{'entries':entries, 'time': datetime.datetime.utcnow()})
    # return render_to_response(html)



def viewallposts(request):
    if request.POST:
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        Postt(title=title, body=body, category=category).save()

    return render_to_response('viewallposts.html', {
        'posts':Postt.objects.all(),
    }, context_instance=RequestContext(request))



def index(request):
    if request.POST:
        title = request.POST['title']
        body = request.POST['body']
        category = request.POST['category']
        Postt(title=title, body=body, category=category).save()

    return render_to_response('index2.html', {
        'posts':Postt.objects.all(),
    }, context_instance=RequestContext(request))


def view_post(request, post_id):
    p = Postt.objects.get(id=post_id)

    if request.POST:
        comment = request.POST['comment']
        Commentt(post=p, comment=comment).save()
    return render_to_response('view_post.html', {
        'p':p,
        'comments': Commentt.objects.filter(post=p),
    }, context_instance=RequestContext(request))


def view_post2(request, post_id):
    p = Postt.objects.get(id=post_id)

    return render_to_response('view_post2.html', {
        'p':p,
        'comments': Commentt.objects.filter(post=p),
    }, context_instance=RequestContext(request))




