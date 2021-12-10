from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Bb

def index(request):
    bbs = Bb.objects.all()
    return render( request, 'index.html', { 'bbs' : bbs })
