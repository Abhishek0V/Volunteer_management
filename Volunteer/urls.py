
from django import views
from django.urls import path,include
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
#usrl here 

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', views.volunteer_login, name='volunteer_login'),
    path('signup/',views.vol_signup,name='Vol_signup'),
    path('logout/', views.volunteer_logout, name='volunteer_logout'),
]
