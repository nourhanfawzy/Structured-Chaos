from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import post
from django.template import Context, loader
from django.http import HttpResponse
import datetime


def home(request):
    # entries = posts.objects.all()
    entries = post.objects.all()
    now = datetime.datetime.now()
    t = get_template('index.html')
    # html = t.render({'posts':entries})
    return render_to_response('index.html',{'entries':entries, 'time': datetime.datetime.utcnow()})
    # return render_to_response(html)
