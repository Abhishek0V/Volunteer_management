
from django import views
from django.urls import path,include
from . import views
#usrl here 

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]
