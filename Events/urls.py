
from django.urls import path,include
from . import views
#usrl here 

urlpatterns = [
    path('', views.home, name="home"),
    path('events/<str:pk>/', views.events, name="events"),
    path('create-event/', views.create_event, name='create_event'),
]
