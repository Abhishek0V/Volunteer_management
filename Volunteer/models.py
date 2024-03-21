from django.db import models
from User.models import User


#model is here-----------

class volunteer(models.Model):
    Gender_type = [
        ("MALE","Male"),
        ("FEMALE","Female"),
        ("OTHERS","Others")
    ]
    user = models.OneToOneField(User, related_name ="vol_profile",on_delete=models.CASCADE)
    Vol_ID = models.BigAutoField(primary_key=True,unique=True)
    Name = models.CharField(max_length=20)
    Gender = models.CharField(choices = Gender_type,max_length=50)
    Age = models.PositiveIntegerField()
    Location = models.CharField(max_length=50)
    profile_img = models.ImageField(upload_to='vol_profile/', null=True, blank=True)

    def __str__(self):
        return self.Name

class Notification(models.Model):
    vol=models.OneToOneField(volunteer,related_name="volunter_model", on_delete=models.CASCADE)
    text=models.CharField(max_length=60,null=True,blank=True)

    def __str__(self):
        return  f"{self.vol.Name}"
