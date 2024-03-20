from django.db import models
from User.models import User

# Create your models here.
class Org(models.Model):
    user =models.OneToOneField(User, related_name = "org_profile", on_delete=models.CASCADE)
    Org_ID = models.BigAutoField(primary_key=True,unique=True)
    Org_Name = models.CharField(max_length = 20)
    Location =models.CharField(max_length=50) 
    verified = models.BooleanField(default =False)
    profile=models.ImageField(upload_to="org_profile/",default="")

    def __str__(self):
        return self.Org_Name