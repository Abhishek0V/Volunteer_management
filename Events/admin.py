from django.contrib import admin
from .models import Events,Registered_volunteers,Gallery
# Register your models here.

admin.site.register(Events)
admin.site.register(Registered_volunteers)
admin.site.register(Gallery)