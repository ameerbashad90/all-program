from re import A
from django.shortcuts import render
from app3.models import *

# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=webpage.objects.all()
    
    d={'ws':webpages}
    return render(request,'display_webpages.html',d)

def display_access(request):
    access=Access_Records.objects.all()
    d={'ac':access}
    return render(request,'display_access.html',d)
