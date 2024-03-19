
from django.urls import path,include
from . import views
#usrl here 

urlpatterns = [
    path('', views.home, name="home"),
    path('events', views.events, name="events"),
]
