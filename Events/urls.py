
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

#usrl here 

urlpatterns = [
    path('', views.home, name="home"),
    path('events/<str:pk>/', views.events, name="events"),
    path('create-event/', views.create_event, name='create_event'),
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
    path('registered_volunteers/<int:event_id>/', views.registered_volunteers, name='registered_volunteers'),
    path('selected_volunteers/<int:event_id>/', views.selected_volunteers, name='selected_volunteers'),
    path('send_notification/<int:event_id>/', views.send_notification, name='send_notification'),
    path('notifications/', views.notification_page, name='notifications'),
    path('gallery/upload/', views.upload, name='add_image'),
    path('gallery/', views.gallery, name='gallery'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
