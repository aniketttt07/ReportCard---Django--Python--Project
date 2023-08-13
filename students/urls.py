from django.urls import path
from .views import *

urlpatterns = [
    path('',table,name='table'),
    path('marks/<sid>/',seemarks,name='seemarks')
    
]
