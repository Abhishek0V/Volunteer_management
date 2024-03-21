from django.db import models
from Org.models import Org 
from Volunteer.models import volunteer
# Create your models here.
class Events(models.Model):
    Event_ID = models.BigAutoField(primary_key=True,unique=True)
    Number_of_Volunteer = models.PositiveIntegerField(verbose_name="Number of Volunteers")
    Size_of_Event = models.PositiveIntegerField(verbose_name="Size of Event")
    Event_Name = models.CharField(max_length=20, verbose_name="Event Name")
    Event_Description = models.TextField(verbose_name="Event Discription", default="")
    Location = models.CharField(max_length=20, verbose_name="Location")
    poster = models.ImageField(upload_to='images/', null=True, blank=True)
    Created_Org = models.ForeignKey(Org, related_name='conducting_Org', on_delete=models.CASCADE) # conducting organization
    Registration_option = models.BooleanField(default = True)
    Event_Date = models.DateTimeField(null = True)
    Event_type = [
        ("PAST","Past"),
        ("COMING","Coming")
    ]
    Event_Status =models.CharField(choices = Event_type ,default = "COMING",max_length = 20) 
    def __str__(self):
        return self.Event_Name
    
class Registered_volunteers(models.Model):
    Event=models.ForeignKey(Events,related_name="event",on_delete=models.CASCADE)
    Volunteers=models.ForeignKey(volunteer,related_name="reg_vols", on_delete=models.CASCADE)
    Selected = models.BooleanField(default = False)

   