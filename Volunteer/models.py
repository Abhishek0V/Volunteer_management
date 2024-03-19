from django.db import models
from User.models import User

#model is here

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
