from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def subbu(request):
    return HttpResponse('<h1>subbu is the new becoming CEO of Google</h1>')

def ramana(request):
    return HttpResponse('hello guys....')