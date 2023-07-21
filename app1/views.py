from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def subbu(request):
    return HttpResponse('<h1> subbu is a good boy...😎😎😎😎</h1>')

def ramana(request):
    return HttpResponse('<h1> ramana is a bad boy...</h1>')