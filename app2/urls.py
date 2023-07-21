from django.urls import path
from app2.views import *

app_name='nothing'

urlpatterns=[
    path('subbu/',subbu,name='subbu'),
    path('ramana/',ramana,name='ramana')
]