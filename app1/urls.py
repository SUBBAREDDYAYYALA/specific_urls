from django.urls import path
from app1.views import *

app_name =' somthing'

urlpatterns=[
    path('subbu/',subbu,name='subbu'),
    path('ramana/',ramana,name='ramana')
]