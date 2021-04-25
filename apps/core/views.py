from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

def home(request):
	return render(request, "core/index.html", {})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)