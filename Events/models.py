from django.db import models
from Org.models import Org 

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