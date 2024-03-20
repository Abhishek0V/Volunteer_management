from . import views
from django.urls import path,include
#usrl here 

urlpatterns = [
    path('signup/', views.org_signup, name='org_signup'),
    
]
