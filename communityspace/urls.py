from django.urls import path
from . import views


urlpatterns = [
    path('', views.community,name='community'),
    path('send/', views.send_message,name='send_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
]