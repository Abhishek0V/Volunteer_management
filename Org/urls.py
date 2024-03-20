from . import views
from django.urls import path,include
#usrl here 

urlpatterns = [
    path("register/",views.org_registration,name="org_register")
    
]
